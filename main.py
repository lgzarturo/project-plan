import datetime
import holidays
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def define_focus_factor(focus_factor: float) -> float:
    """
    Define el factor de enfoque para que sea un valor entre 0 y 1
    :param focus_factor: factor de enfoque
    :return: float
    """
    if focus_factor > 100:
        return 1
    if focus_factor > 1:
        return focus_factor / 100
    return focus_factor


def input_project_details() -> tuple:
    """
    Solicita al usuario los detalles del proyecto y los devuelve como una tupla
    :return: tuple
    """
    start_date = input(
        "Ingresa la fecha de inicio del proyecto (dd/mm/yyyy) o si deseas usar la fecha actual presiona enter: "
    )
    if not start_date:
        start_date = datetime.datetime.now().strftime("%d/%m/%Y")
    number_of_devs = int(
        input("Ingresa el número de desarrolladores que trabajarán en el proyecto: ")
    )
    personal_focus_factor = [
        float(
            input(f"Ingresa el factor de enfoque personal del desarrollador {i + 1}: ")
        )
        for i in range(number_of_devs)
    ]
    personal_focus_factor = [
        define_focus_factor(factor) for factor in personal_focus_factor
    ]
    project_focus_factor = define_focus_factor(
        float(input("Ingresa el factor de enfoque del proyecto: "))
    )

    tasks = []
    while True:
        task_name = input("Ingresa el nombre de la tarea: ")
        task_points = float(input("Ingresa los puntos de la tarea: "))
        tasks.append((task_name, task_points))
        if input("¿Deseas agregar otra tarea? (s/n): ").lower() == "n":
            break

    support_time = float(input("Ingresa el tiempo de soporte en número de días: "))
    testing_time = float(input("Ingresa el tiempo de pruebas en número de días: "))

    return (
        start_date,
        number_of_devs,
        personal_focus_factor,
        project_focus_factor,
        support_time,
        testing_time,
        tasks,
    )


def calculate_working_days(
    start_date: datetime.date, total_hours: float, holidays: list[datetime.date]
) -> tuple:
    """
    Calcula la fecha de finalización del proyecto y los días laborales necesarios
    :param start_date: fecha de inicio del proyecto
    :param total_hours: cantidad total de horas necesarias para completar el proyecto
    :param holidays: lista de días festivos
    :return: tuple
    """
    end_date = start_date
    hours_remaining = total_hours
    working_days = 0
    while hours_remaining > 0:
        end_date += datetime.timedelta(days=1)
        compare_date = end_date
        if isinstance(compare_date, datetime.datetime):
            compare_date = compare_date.date()
        if end_date.weekday() < 5 and compare_date not in holidays:
            working_days += 1
            hours_remaining -= 8
    return end_date, working_days


def calculate_project_end_date(
    start_date: datetime.date,
    number_of_devs: int,
    personal_focus_factor: list[float],
    project_focus_factor: float,
    support_time: float,
    testing_time: float,
    tasks: list,
) -> tuple:
    """
    Calcula la fecha de finalización del proyecto y las fechas de finalización de las tareas
    :param start_date: fecha de inicio del proyecto
    :param number_of_devs: número de desarrolladores
    :param personal_focus_factor: cantidad de enfoque personal de cada desarrollador
    :param project_focus_factor: factor de enfoque del proyecto
    :param support_time: tiempo de soporte en días
    :param testing_time: tiempo de pruebas en días
    :param tasks: lista de tareas
    :return:
    """
    total_focus_factor = sum(personal_focus_factor) / number_of_devs
    daily_effort = total_focus_factor * project_focus_factor * 8
    total_points = sum([points for _, points in tasks])
    total_hours = (total_points + support_time + testing_time) / daily_effort * 8
    holidays_mx = holidays.MX(years=[start_date.year])
    end_date, working_days = calculate_working_days(
        start_date, total_hours, holidays_mx
    )

    task_end_dates = []
    task_hours_remaining = [points / daily_effort * 8 for _, points in tasks]
    task_hours_remaining.append(support_time / daily_effort * 8)
    task_hours_remaining.append(testing_time / daily_effort * 8)

    for hours in task_hours_remaining:
        if hours > 0:
            end_date, working_days = calculate_working_days(
                end_date, hours, holidays_mx
            )
            task_end_dates.append(end_date)

    return total_points, task_end_dates


def generate_gantt_chart(
    tasks: list, task_end_dates: list[datetime.date], start_date: datetime.date
) -> None:
    """
    Genera un diagrama de Gantt para visualizar las tareas y sus fechas de finalización
    :param tasks: lista de tareas
    :param task_end_dates: fechas de finalización de las tareas
    :param start_date: fecha de inicio del proyecto
    :return: None
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    current_start_date = start_date
    for i, ((task_name, _), end_date) in enumerate(zip(tasks, task_end_dates)):
        start = mdates.date2num(current_start_date)
        end = mdates.date2num(end_date)
        duration = end - start
        ax.barh(
            i,
            duration,
            left=start,
            height=0.5,
            align="center",
            color="blue",
            alpha=0.8,
        )
        ax.text(
            start + duration / 2,
            i,
            task_name,
            ha="center",
            va="center",
            color="white",
        )
        current_start_date = end_date
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task_name for task_name, _ in tasks])
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    plt.xlabel("Fecha")
    plt.ylabel("Tareas")
    plt.title("Diagrama de Gantt del proyecto")
    plt.show()


def generate_burndown_chart(total_points, tasks, task_end_dates, start_date) -> None:
    dates = [start_date + datetime.timedelta(days=i) for i in range((task_end_dates[-1] - start_date).days + 1)]
    work_remaining = [total_points] * len(dates)
    current_points = total_points
    for date in dates:
        for end_date, (title, points) in zip(task_end_dates, tasks):
            if date >= end_date:
                current_points -= points
        work_remaining[dates.index(date)] = current_points

    plt.figure(figsize=(10, 6))
    plt.plot(dates, work_remaining, label="Trabajo pendiente")
    plt.xlabel("Fecha")
    plt.ylabel("Puntos de historia restantes")
    plt.title("Gráfico de Burndown del proyecto")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Se solicitan los detalles del proyecto
    (
        start_date,
        number_of_devs,
        personal_focus_factor,
        project_focus_factor,
        support_time,
        testing_time,
        tasks,
    ) = input_project_details()
    print(
        start_date,
        number_of_devs,
        personal_focus_factor,
        project_focus_factor,
        support_time,
        testing_time,
        tasks,
    )
    # Se convierte la fecha de inicio a un objeto datetime
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()

    # Se calcula la fecha de finalización del proyecto y las fechas de finalización de las tareas
    total_points, task_end_dates = calculate_project_end_date(
        start_date,
        number_of_devs,
        personal_focus_factor,
        project_focus_factor,
        support_time,
        testing_time,
        tasks,
    )

    # Se imprime la fecha de finalización del proyecto y las fechas de finalización de las tareas
    print(f"\nTotal de puntos de historia del proyecto: {total_points}")
    for i, (task_name, end_date) in enumerate(zip(tasks, task_end_dates)):
        print(f"-- Tarea {task_name[0]} terminará en {end_date.strftime('%d/%m/%Y')}")
    print(f"\nFecha final del proyecto: {task_end_dates[-1].strftime('%d/%m/%Y')}")

    # Se genera un diagrama de Gantt para visualizar las tareas y sus fechas de finalización
    generate_gantt_chart(tasks, task_end_dates, start_date)

    # Se genera un gráfico de Burndown para visualizar el progreso del proyecto
    generate_burndown_chart(total_points, tasks, task_end_dates, start_date)

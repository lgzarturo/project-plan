# Proyecto de Gestión de Tareas y Generación de Diagrama de Gantt

## Objetivos

- Este proyecto tiene como objetivo ser una herramienta para la gestión de proyectos de software.
- Se basa en calcular el tiempo que se tarda en realizar una tarea, tomando en consideración los puntos de historia de cada tarea, asi como el focus factor, el tiempo de soporte y el tiempo de pruebas.
- El script solicita los datos de entrada para definir el proyecto, y luego calcula el tiempo total que se tardará en realizar el proyecto.
- Se usa la metodología de puntos de historia para estimar el tiempo que se tarda en realizar una tarea. Se toma en cuenta el focus factor, el tiempo de soporte y el tiempo de pruebas.
- Generar un diagrama de Gantt con la planificación del proyecto.

## Descripción
Este script en Python permite gestionar proyectos ingresando detalles como la fecha de inicio, número de desarrolladores, factores de enfoque, tareas, tiempo de soporte y tiempo de pruebas. Calcula la fecha de finalización del proyecto y las fechas de finalización de cada tarea, y genera un diagrama de Gantt para visualizar las tareas.

## Requisitos
- Python 3.x
- Librerías: `datetime`, `holidays`, `matplotlib`
- Pipenv para el entorno de desarrollo

## Uso

1. Ejecuta el script `python3 main.py`.
2. Ingresa los detalles del proyecto cuando se te solicite:
   - Fecha de inicio del proyecto
   - Número de desarrolladores
   - Factores de enfoque personales
   - Factor de enfoque del proyecto
   - Tareas con sus puntos correspondientes
   - Tiempo de soporte
   - Tiempo de pruebas
3. El script calculará la fecha de finalización del proyecto y las fechas de finalización de cada tarea.
4. Se generará un diagrama de Gantt para visualizar las tareas y sus fechas de finalización.

## Funciones importantes

### `define_focus_factor(focus_factor: float) -> float`
Ajusta el factor de enfoque para que sea un valor entre 0 y 1.

### `input_project_details() -> tuple`
Solicita al usuario ingresar los detalles del proyecto y devuelve una tupla con esos detalles.

### `calculate_project_end_date(start_date, number_of_devs, personal_focus_factor, project_focus_factor, support_time, testing_time, tasks)`
Calcula la fecha de finalización del proyecto y las fechas de finalización de cada tarea.

### `generate_gantt_chart(tasks, task_end_dates, start_date)`
Genera un diagrama de Gantt para visualizar las tareas y sus fechas de finalización.

## Metodología Utilizada

Este script sigue un enfoque similar a las metodologías ágiles como Scrum y Kanban para la estimación y gestión del tiempo del proyecto.

## Fórmulas

**Teoría**: Las fórmulas en el script parecen alinearse más con una metodología de estimación de tiempos basada en la capacidad y el rendimiento del equipo, a menudo utilizada en metodologías ágiles como Scrum o Kanban. Aquí hay un desglose y explicación de cómo estas metodologías se relacionan con las fórmulas del script:

### Capacidad del Proyecto

- En Scrum y Kanban, la capacidad del equipo se calcula en función de la disponibilidad y el enfoque de los miembros del equipo.

```
# Formula original
project_capacity = sum(personal_focus_factor) * project_focus_factor * number_of_devs
```

- En el script, se calcula el factor de enfoque y después se obtiene el esfuerzo diario, como modificación de la formula original, luego se obtienen la horas totales en base al esfuerzo, los puntos de historia, para realizar el calculo de las horas restantes que servira para deteminar los dias que de trabajo.

### Duración de Tareas

- En las metodologías ágiles, la duración de las tareas se puede calcular dividiendo los puntos de historia (o puntos de tarea) por la capacidad del equipo. Esto es similar a cómo el script calcula la duración de las tareas:

```
# Formula original
duration = task_points / project_capacity
```

### Fecha de Finalización de Tareas

- En Scrum y Kanban, se suele utilizar un enfoque iterativo y se considera la disponibilidad del equipo en días laborables. En el script, se excluyen los fines de semana y festivos:

La fecha de finalización de cada tarea se obtiene sumando la duración de la tarea a la fecha de inicio de la tarea, excluyendo días no laborables y festivos.

Se incrementa la fecha actual (current_start_date) excluyendo días no laborables y festivos:

```
end_date = start_date + duration_tasks  # considerando días laborables y festivos
```

### Puntos de historía

**Metodologías Ágiles**: A menudo utilizan una única estimación basada en la capacidad y los puntos de historia, lo cual es más directo y simple.

## Mejoras

- [ ] Realizar una estimación en base a la metodología PERT.
- [ ] Agregar la posibilidad de exportar a Excel o CSV.
- [ ] Integrar más variables a la estimación de tiempos.
- [ ] Soporte de trabajo en paralelo.
- [ ] Mejorar la visualización del diagrama de Gantt.
- [ ] Añadir la capacidad de definir dependencias entre las tareas, para determinar que tareas deben completarse antes que otras.
- [ ] Asignar roles especificos como frontend, backend, ux para mejorar la estimación.
- [ ] Para facilitar el calculo, hice que fuera el promedio en base al factor de esfuerzo, seria mejore permitir el calculo de la capacidad individual de cada desarrollador.
- [ ] Pensar en un formato de historias de usuario, para que las estimaciones esten basadas en dichas historias, sus puntos y considerando la complejidad de cada tarea.

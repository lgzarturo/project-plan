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

## Uso

1. Ejecuta el script.
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

## Fórmulas

### Capacidad del Proyecto
\[ \text{Capacidad} = \sum (\text{Factor de Enfoque Personal}) \times \text{Factor de Enfoque del Proyecto} \times \text{Número de Desarrolladores} \]

### Duración de Tareas
\[ \text{Duración de la Tarea} = \frac{\text{Puntos de la Tarea}}{\text{Capacidad del Proyecto}} \]

### Fecha de Finalización de Tareas
La fecha de finalización de cada tarea se obtiene sumando la duración de la tarea a la fecha de inicio de la tarea, excluyendo días no laborables y festivos.

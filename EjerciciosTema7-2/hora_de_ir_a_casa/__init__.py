from datetime import datetime


def es_la_hora_de_ir():
    # Obtener la hora actual
    now = datetime.now()
    hora_actual = now.hour

    hora_de_salida = 19

    # Calcular la hora que falta hasta la medianoche
    hours_left = hora_de_salida - hora_actual - 1
    minutes_left = 60 - now.minute

    if now.hour < hora_de_salida:
        print(f"Faltan {hours_left} horas y {minutes_left} minutos para salir a las {hora_de_salida}:00 horas.")
    else:
        print("Si ya tener que ir para casa. ;-)")

# Importar librerías.
from datetime import datetime

# Definir función para formatear y retornar mensaje a partir de la fecha y hora actual.
def mensaje_fecha_hora_actual (fecha_hora_actual):
    meses = ["Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dia = fecha_hora_actual.day
    mes = meses[fecha_hora_actual.month - 1]
    anio = fecha_hora_actual.year
    if (fecha_hora_actual.hour < 10):
        hora = "0" + str(fecha_hora_actual.hour)
    else:
        hora = str(fecha_hora_actual.hour)
    if (fecha_hora_actual.minute < 10):
        minuto = "0" + str(fecha_hora_actual.minute)
    else:
        hora = str(fecha_hora_actual.minute)
    msj = "La fecha y hora actual es: {}:{} del {} de {} del {}".format(hora, minuto, dia, mes, anio)
    return msj

# Obtener la fecha y hora actual.
ahora = datetime.now()
# Generar el mensaje formateado a partir de la fecha y hora actual, usando la función creada.
mensaje = mensaje_fecha_hora_actual(ahora)
# Imprimir mensaje por pantalla.
print(mensaje)
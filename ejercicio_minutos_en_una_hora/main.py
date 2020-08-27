import sys

# Pedir al usuario ingresar la cantidad de horas.
entrada_horas = input("Ingrese una cantidad de horas: ")

try:
    # Convertir cadena de entrada de horas en número.
    horas = int(entrada_horas)
except ValueError:
    print("ERROR: No ha ingresado un número válido.")
    sys.exit(1)

# Validar que las horas ingresadas estén entre 0 y 100, sin incluír ambos límites.
# Si no se cumple esta condición, el programa termina de ejecutarse.
if (0 < horas < 100):
    # Convertir las horas a minutos.
    minutos = horas * 60
    
    # Imprimir en pantalla los minutos calculados.
    if horas == 1:
        print(f"Existen {minutos} minutos en {horas} hora.")
    else:
        print(f"Existen {minutos} minutos en {horas} horas.")
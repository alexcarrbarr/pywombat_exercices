# Importar librerías.
import random

# Definir función para generar números aleatorios.
def aleatorios (cantidad = 5):
    return random.sample(range(1, 101), cantidad)

# Pedir al usuario la cantidad de números a generar.
entrada = input("Ingresa la cantidad de números a generar (opcional; para no ingresar cantidad, sólo presiona Entrar): ")

numerosAleatorios = []
# Si la entrada está vacía, entonces generar una cantidad por defecto de números aleatorios dentro del rango 1 a 100.
if (not entrada):
    numerosAleatorios = aleatorios()
else: # Si no, entonces generar la cantidad requerida de números aleatorios dentro del rango 1 a 100.
    cantidad = int(entrada)
    numerosAleatorios = aleatorios(cantidad)

# Recorrer los números aleatorios generados e imprimirlos en pantalla.
print(f"for number in aleatorios({entrada}):")
for i in range(0, len(numerosAleatorios)):
    print(numerosAleatorios[i])
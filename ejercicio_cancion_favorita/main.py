# Importar librerías.
import random

# Crear lista de canciones.
listaCanciones = []

# Pedir 10 veces al usuario, canciones para agregar a la lista.
for i in range(0, 10):
    temp = input("Ingresa una canción: ")
    listaCanciones.append(temp)

# Seleccionar al azar una canción de la lista.
seleccion = random.choice(listaCanciones)

# Mostrar la canción seleccionada.
print("")
print(f"Debes escuchar ahora: {seleccion}")
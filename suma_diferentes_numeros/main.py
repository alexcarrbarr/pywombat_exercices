a = int(input("Ingresa un número: "))
b = int(input("Ingresa un número: "))
c = int(input("Ingresa un número: "))
suma = 0
if (not (a == b and b == c)):
    suma = a
    if (b != a):
        suma += b
    if (c != a and c != b):
        suma += c
print(f"Resultado: {suma}")
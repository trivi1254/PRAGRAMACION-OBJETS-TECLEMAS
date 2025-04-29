inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))
contador = 0  # Variable para contar pares
for i in range(inicio, fin + 1):  # Itera entre inicio y fin
    if i % 2 == 0:  # Verifica si el número es par
        contador += 1  # Incrementa el contador
print(f"Hay {contador} números pares entre {inicio} y {fin}.")
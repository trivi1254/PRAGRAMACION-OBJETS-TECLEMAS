n = int(input("Ingrese cuántos números desea al cuadrado: "))
cuadrados = []  # Lista para almacenar los resultados
for i in range(1, n + 1):  # Itera hasta n
    cuadrados.append(i ** 2)  # Calcula el cuadrado y lo agrega a la lista
print(f"Los cuadrados de los números del 1 al {n} son: {cuadrados}")

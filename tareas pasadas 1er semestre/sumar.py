# Definición de la función
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b


# Uso de la función
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
print("1.suma")
print("2.restar")
print("3.multiplicacion")
print("4.division")

opcion=int(input("seleccione una opcion : "))

if opcion == 1:
    resultado = sumar(numero1, numero2)
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == 2:
    resultado = restar(numero1, numero2)
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif opcion == 3:
    resultado = multiplicacion(numero1, numero2)
    print(f"La multiplicacion de {numero1} y {numero2} es: {resultado}")
elif opcion == 4:
    resultado = division(numero1, numero2)
    print(f"la division de {numero1} y {numero2} es: {resultado}")
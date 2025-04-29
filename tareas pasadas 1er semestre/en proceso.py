# Calculadora de Divisas

print("Bienvenido a la calculadora de divisas")
print("Opciones disponibles:")
print("1. Dólares a Euros")
print("2. Euros a Dólares")

# Selección del usuario
opcion = int(input("Elige una opción (1 o 2): "))

if opcion == 1:
    # Conversión de Dólares a Euros
    dolares = float(input("Ingresa la cantidad en dólares: "))
    tasa_cambio = 0.85  # Ejemplo de tasa de cambio
    euros = dolares * tasa_cambio
    print(f"{dolares} dólares son aproximadamente {euros:.2f} euros.")
elif opcion == 2:
    # Conversión de Euros a Dólares
    euros = float(input("Ingresa la cantidad en euros: "))
    tasa_cambio = 1.18  # Ejemplo de tasa de cambio
    dolares = euros * tasa_cambio
    print(f"{euros} euros son aproximadamente {dolares:.2f} dólares.")
else:
    print("Opción no válida. Por favor, elige 1 o 2.")

print("Gracias por usar la calculadora de divisas.")
while True:
    print("\n--- MENÚ DE OPERACIONES MATEMÁTICAS ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. division")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La resta es: {a - b}")
    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {a * b}")
    elif opcion == 4:
        a= float(input("ingrese el primer numero: "))
        b= float(input("ingrese el segundo  numero: "))
        print(f"La division es: {a / b}")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
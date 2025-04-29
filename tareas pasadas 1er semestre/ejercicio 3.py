matematica = float(input("Ingrese su calificación en Matemática: "))
programacion = float(input("Ingrese su calificación en Programación: "))

# Evaluar resultados
if matematica >= 7:
    if programacion >= 7:
        print("¡Aprobaste ambas materias!")
    else:
        print("Aprobaste Matemática, pero reprobaste Programación.")
else:
    if programacion >= 7:
        print("Reprobaste Matemática, pero aprobaste Programación.")
    else:
        print("Reprobaste ambas materias.")
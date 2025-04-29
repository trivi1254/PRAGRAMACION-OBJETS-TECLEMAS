# Definición de la función
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Uso de la función
numero = 8
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
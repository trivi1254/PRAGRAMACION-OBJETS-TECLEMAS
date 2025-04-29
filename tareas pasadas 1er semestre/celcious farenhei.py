# Definición de la función
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Uso de la función
temperatura_celsius = 10
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit}°F.")
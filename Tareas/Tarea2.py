cant = 0
suma = 0
lecturas = [] #lista para guardar los valores

NOMBRE = input("Nombre y Apellido: ")
EQUIPO = int(input("Número de equipo(e.j: 12): "))

while True:
    entrada = input("Ingrese los voltajes obtenidos en la práctica de laboratorio (Escriba FIN si escribió todos sus valores): ")
    if entrada.upper() == "FIN":
        break
    try:
        mues = float(entrada)
        lecturas.append(mues)
        cant = cant + 1
        suma = suma + mues
    except ValueError:
        print("Valor no válido, intente de nuevo.")

promedio = suma / cant

if promedio >= 15:
    umbral = "ALTO (>= 15.00 V)"
elif promedio >= 10:
    umbral = "MEDIO (<= 15.00 V ʌ >= 10.00 V)"
else:
    umbral = "BAJO (<= 10.00 V)"


print("=== REPORTE DEL SENSOR ===")
print(f"Nombre:  {NOMBRE} | Equipo: UT-{EQUIPO}")
print(f"Lecturas(V): {lecturas} | Promedio: {promedio:.2f}V")
print(f"Estado: {umbral}")


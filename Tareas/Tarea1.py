import datetime as dt
import random as rd
nombre = "Marcelo Cuzcano Mostacero"
fecha = dt.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
print(fecha)
print("Saludos cordiales Ing. Juan, en este correo adjunto los valores de tensiones obtenidos: ")

for i in range(15):
    v = rd.randint(0,220)
    if v <= 73:
        print("Valor bajo: " + str(v))
    elif v <= 146:
        print("Valor medio: " + str(v))
    else:
        print("Valor alto: " + str(v))

print("Gracias,")
print(nombre)



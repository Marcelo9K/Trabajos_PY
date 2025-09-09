valor_txt=input("Ingrese los valores en C: ")
try:
    t=float(valor_txt)
    if t >= 30: 
        print("Alerta!")
    elif t < 0:
        print("Temperatura bajo 0")
    else:
        print("Temperatura normal")
except ValueError:
    print("Entrada inválida. Use números (ej. 26.5).")
from pathlib import Path #importo el comando path (busca el lugar del codigo)
ROOT=Path(__file__).resolve().parents[1]#busca el lugar donde esta guardado el codigo
TXT=ROOT/"Archivos"/"mediciones_basico.txt" #"Archivos" debe cambiar dependiendo de la ubicación del archivo
#comentarios=0
valores = []
with open(TXT,"r",encoding='utf-8') as f:
    for linea in f: #"linea" lee linea por linea hasta acabar el documento
        s=linea.strip() #elimina lineas vacias
        #no guardo en memoria los valores con comentario # o !
        if not s or s.startswith("#"):
            #comentarios=comentarios+1
            continue
        if not s or s.startswith("!"):
            #comentarios=comentarios+1
            continue
        #reemplaza las comas por puntos
        s=s.replace(",",".")    #Reemplaza comas por puntos decimales
        try:
            valores.append(float(s)) #si cumple las condiciones se graba en valores
                                        # float para convertir a numeros decimales
        except ValueError:
            #si no es ni linea ni numero, debe saltarlo
            pass
    
Vmayor=[]
Vmenor=[]
for i in valores:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)

print(len(Vmayor))
print(len(Vmenor))

#print(f"el numero de alertas para voltajes mayores a 5V es: {len(Vmayor)}")

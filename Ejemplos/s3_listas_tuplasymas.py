#lista - Mutables
Cod22561=["Juan",35,"Ing. Ambiental",975666666] #listas si cambian
#Lista=[0,1,2,3]
print(f"la edad de {Cod22561[0]} es: {Cod22561[1]}, su numero es el {Cod22561[3]} y es un {Cod22561[2]}")
Cod22561[2]="Mg en ing. Ambiental"
#Archivos tipo CVS
#Tuplas - No son mutables
CodJefe=("Pedro",65,"Administrador",939333874) #tupla no cambia
print(f"la edad de {CodJefe[0]} es: {CodJefe[1]} y su numero es el {CodJefe[3]}")

#diccionarios - son mutables y le dan un nombre a cada indice 
CodNuevo={"nombre":"Ricardo","Edad":19,"Carrera":"Programador","Telefono":998776554}
CodNuevo["Carrera"]="Ing Bailarin"
print(f"la edad de {CodNuevo['nombre']} es: {CodNuevo['Edad']}, su numero es el {CodNuevo['Telefono']} y es {CodNuevo['Carrera']}")
#archivos tipo JSON

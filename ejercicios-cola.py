from tda_cola import Cola, arribo, atencion, cola_llena, cola_vacia, tamanio, en_frente, mover_final
from random import randint
from tda_pila import Pila,pila_llena, pila_vacia, desapilar, apilar
import time
c = Cola()
p= Pila()

#Ejercicio 1
"""
cont=0
vocales= ["a","e","i","o","u"]

while not cola_llena(c):
    x= chr(randint(65,122))
    arribo(c, x)

largo=tamanio(c)
while cont<largo:
    cont+=1
    x= en_frente(c)
    if x.lower() in vocales:
        atencion(c)
    else:
        mover_final(c)

while not cola_vacia(c):
    x=atencion(c)
    print(x)
"""

#Ejercicio 2
""""
while not cola_llena(c):
    x= randint(65,122)
    arribo(c, x)
    print(x)

while not cola_vacia(c):
    x=atencion(c)
    apilar(p,x)
print("------------------------------")
while not pila_vacia(p):
    x= desapilar(p)
    arribo(c,x)
    print(x)

"""
#Ejercicio 3
"""
flag= True
cont=0
x=input("Ingrese una palabra: ")
for i in x:
    arribo(c,i)

while cont< len(x):
    aux= mover_final(c)
    apilar(p,aux)
    cont+=1

while not pila_vacia(p):
    aux= desapilar(p)
    if aux != atencion(c):
        flag= False
    
if flag:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")

"""

#Ejercicio 4

"""
cont=0

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

while not cola_llena(c):
    arribo(c,randint(1,100))

while cont<=tamanio(c):
    cont+=1
    x=en_frente(c)
    if isPrime(x):
        mover_final(c)
    else:
        atencion(c)
        cont-=1 

while not cola_vacia(c):
    x = atencion(c)
    print(x)

"""

#Ejercicio 5
"""

while not pila_llena(p):
    x= randint(1,100)
    print(x)
    apilar(p, x)

while not pila_vacia(p):
    x=desapilar(p)
    arribo(c,x)

while not pila_llena(p):
    x= atencion(c)
    apilar(p,x)

print("------------------------------------------")

while not pila_vacia(p):
    x=desapilar(p)
    print(x)

"""

#Ejercicio 6
"""
cont=0
while not cola_llena(c):
    x= randint(1, 10)
    print(x)
    arribo(c,x)
x= int(input("Ingrese el elemento que desea buscar en la lista: "))

for i in range(0, c.tamanio):
    aux=mover_final(c)
    if x == aux:
        cont+=1
print("El elemento {} aparece {} veces.".format(x,cont))
"""
#Ejercicio 7
"""
cont=0
while not cola_llena(c):
    x= randint(1, 100)
    print(x)
    arribo(c,x)

aux=int(input("Ingrese el numero del elemento despues del frente de la cola que desea eliminar: "))

for i in range(0, c.tamanio):
    if cont == aux:
        atencion(c)
    else:
        mover_final(c)
    cont+=1

while not cola_vacia(c):
    x=atencion(c)
    print(x) 
"""
#Ejercicio 8
"""
x= randint(1, 100)
arribo(c,x)
chico= x
while not cola_llena(c):
    cont=0
    x= randint(1, 100)
    aux= atencion(c)
    if x<chico:
        chico=x

    while aux < x and cont < c.tamanio:
        cont+=1
        arribo(c,aux)
        aux= atencion(c)
    
    if aux<x: 
        arribo(c,aux)
        arribo(c,x)
    else: 
        arribo(c,x)
        arribo(c,aux)
    
    while en_frente(c) != chico:
        mover_final(c)

while not cola_vacia(c):
    x= atencion(c)
    print(x)

"""
#Ejercicio 9

"""
cont=0
contneg=0

while not cola_llena(c):
    x= randint(-100, 100)
    arribo(c,x)

x= mover_final(c)
maschico=x
masgrande=x

while cont != c.tamanio:
    cont+=1
    x=mover_final(c)
    if x<0:
        contneg+=1
    if x<maschico:
        maschico=x
    if x>masgrande:
        masgrande=x

while not cola_vacia(c):
    x= atencion(c)
    print(x)

print("--------------")
print("Numeros negativos: ",contneg)
print("Rango de valores: ",masgrande-maschico)
"""
#Ejercicio 10
"""
class Personajes():
    def __init__(self):
        self.nombre,self.planeta="", ""

def persPlaneta(planeta):
    cont=0
    print("Personajes del planeta {}:".format(planeta))
    while cont != c.tamanio:
        x= Personajes()
        cont+=1
        x= mover_final(c)
        if x.planeta == planeta:
            print(x.nombre)

def natal(c,pers):
    cont=0
    while cont != c.tamanio:
        x= Personajes()
        x= mover_final(c)
        cont+=1
        if x.nombre == pers:
            print("EL planeta natal de {}, es: {}".format(x.nombre,x.planeta))

def agregar(c,pers): #No funciona
    tamanioo=c.tamanio
    cont=0
    print("Se agregara un personaje antes de ",pers,". Solo si este se encuentra en la lista")
    salir= False
    while cont < tamanioo and not salir:
        aux= Personajes()
        cont+=1
        aux= en_frente(c)
        print("---------",aux.nombre)
        if aux.nombre == pers:
            x=Personajes()
            x.nombre=input("Nombre:")
            x.planeta=input("Planeta: ")
            arribo(c,x)
            print("Personaje agregado")
            salir=True
        mover_final(c)

    while c.tamanio > cont:
        cont+=1
        mover_final(c)

def eliminar(pers):
    cont=0
    while cont<= c.tamanio:
        cont+=1
        x=Personajes()
        x=mover_final(c)
        if x.nombre == pers:
            atencion(c)
            cont+=1

while not cola_llena(c):
    x= Personajes()
    x.nombre=input("Nombre: ")
    x.planeta=input("Planeta: ")
    arribo(c,x)

persPlaneta("Alderaan")
persPlaneta("Endor")
persPlaneta("Tatooine")
natal(c,"Han Solo")

#agregar(c,"maestro Yoda")
eliminar("Jar Jar Binks")

while not cola_vacia(c):
    asdx= Personajes()
    asdx= atencion(c)
    print(asdx.nombre, asdx.planeta)
"""
#Ejercicio 11
"""
c2= Cola()
c3= Cola()
x=0
x2=0
print("cola 1")
while not c.tamanio==5:
    x+=2
    print(x)
    arribo(c,x)
print("cola 2")
while not c2.tamanio==5:
    x2+=3
    print(x2)
    arribo(c2,x2)

while not cola_vacia(c)and not cola_vacia(c2):
    if en_frente(c) < en_frente(c2):
        x=atencion(c)
        arribo(c3,x)
    else:
        x=atencion(c2)
        arribo(c3,x)

while not cola_vacia(c):
    x=atencion(c)
    arribo(c3,x)
while not cola_vacia(c2):
    x=atencion(c2)
    arribo(c3,x)

print("cola 3")
while not cola_vacia(c3):
    x= atencion(c3)
    print(x)
"""
#Ejercicio 12
"""
caracter1= False
caracter2= False
cdigit= Cola()
resto= Cola()
cont=0
while not cola_llena(c):
    x= randint(33,122)
    arribo(c,chr(x))

while not cola_vacia(c):
    x=atencion(c)
    if x.isdigit():
        arribo(cdigit,x)
    else:
        arribo(resto,x)
        if x.islower or x.issuper:
            cont+=1
        if x == "#":
            caracter1= True
        elif x == "?":
            caracter2= True

print("Cola de digitos: ")

while not cola_vacia(cdigit):
    x=atencion(cdigit)
    print(x)

print("Cola de resto de caracteres: ")

while not cola_vacia(resto):
    x=atencion(resto)
    print(x)

print("En la segunda cola aparecen {} letras".format(cont))

if caracter1:
    print("El caracter #, aparece en la cola de caracteres")
else: 
    print("El caracter #, no aparece en la cola de caracteres")

if caracter2:
    print("El caracter ?, aparece en la cola de caracteres")
else: 
    print("El caracter ?, no aparece en la cola de caracteres")
"""
#Ejercicio 16
"""
class Procesos():
    def __init__(self):
        self.name,self.time= "", 0.0
    
while not cola_llena(c):
    x= Procesos()
    x.name= input("Proceso: ")
    x.time= float(input("Tiempo: "))
    arribo(c,x)

while not cola_vacia(c):
    agregar= False
    x = Procesos()
    x= atencion(c)
    print("Atendiendo {}...".format(x.name))
    print(x.time)
    if (x.time <= 4.5):
        time.sleep(x.time)
        agregar= True
    else:
        time.sleep(4.5)
        x.time= x.time-(4.5)
        arribo(c,x)
        print("Quantum exedido, devolviendo a la cola con el tiempo restado")

    if not cola_llena(c) and agregar:
        res=input("Desea agregar un nuevo proceso? Y/N: ")
        if res.upper() == "Y":
            x = Procesos()
            x.name= input("Proceso: ")
            x.time= float(input("Tiempo: "))
            arribo(c,x)

print("Procesos terminados :D ")
"""
#Ejercicio 17 
"""
colaACF= Cola()
colaBDE= Cola()
A,B,C,D,E,F=0,0,0,0,0,0

while not cola_llena(c):
    aux= ""
    x= randint(65,70)
    aux+=chr(x)
    x=randint(000,999)
    if len(str(x))==1:
        aux+="00"
        aux+=str(x)
    elif len(str(x))==2:
        aux+="0"
        aux+=str(x)
    else:
        aux+=str(x)

    arribo(c,aux)

while not cola_vacia(c):
    x= atencion(c)
    if x[0]=="A" or x[0]=="C" or x[0]=="F":
        if x[0]=="A":
            A+=1
        elif x[0]=="C":
            C+=1
        else:
            F+=1
        arribo(colaACF,x)
    elif x[0]=="B" or x[0]=="D" or x[0]=="E":
        if x[0]=="B":
            B+=1
        elif x[0]=="D":
            D+=1
        else:
            E+=1
        arribo(colaBDE,x)

if colaACF.tamanio>colaBDE.tamanio:
    print("La cola con turnos comenzados por A,C,F tiene mas turnos")
    if A>C and A>F:
        print("Hay mayor cantidad de turnos empezado por A")
    elif C>F:
        print("Hay mayor cantidad de turnos empezado por C")
    else:
        print("Hay mayor cantidad de turnos empezado por F")
    while not cola_vacia(colaBDE):
        x= atencion(colaBDE)
        if int(x[1:4]) >= 506:
            print(x)
else:
    print("La cola con turnos comenzados por B,E,D tiene mas turnos")
    if B>E and B>D:
        print("Hay mayor cantidad de turnos empezado por B")
    elif E>D:
        print("Hay mayor cantidad de turnos empezado por E")
    else:
        print("Hay mayor cantidad de turnos empezado por D")
    while not cola_vacia(colaACF):
        x= atencion(colaACF)
        if int(x[1:4]) >= 506:
            print(x)
"""
#Ejercicio 19
"""
c2= Cola()
c3= Cola()

recaudo1,recaudo2,recaudo3=0,0,0

veiculos= [["Automovil",47],["Camioneta",59],["Camion",71],["Colectivo",64]]

def peaje(cola,numerodecola):
    autos,camionetas,camiones,colectivos,recaudo=0,0,0,0,0
    while not cola_vacia(cola):
        x=atencion(cola)
        recaudo+= x[1]
        if x[0]== "Automovil":
            autos+=1
        elif x[0]== "Camioneta":
            camionetas+=1
        elif x[0]== "Camion":
            camiones+=1
        elif x[0]== "Colectivo":
            colectivos+=1

    print("En la cabina {} pasaron: ".format(numerodecola))
    print("Automoviles: ",autos)
    print("Camioneta : ",camionetas)
    print("Camion: ",camiones)
    print("Colectivo: ",colectivos)
    return recaudo

while not cola_llena(c):
    x=veiculos[randint(0,3)]
    arribo(c,x)

while not cola_llena(c2):
    x=veiculos[randint(0,3)]
    arribo(c2,x)

while not cola_llena(c3):
    x=veiculos[randint(0,3)]
    arribo(c3,x)

recaudo1=peaje(c,1)
recaudo2=peaje(c2,2)
recaudo3=peaje(c3,3)   

if recaudo1 > recaudo2 and recaudo1 > recaudo3:
    print("La cabina 1 fue la que mas recaudo con un total de: $",recaudo1)
elif recaudo2 > recaudo3:
    print("La cabina 2 fue la que mas recaudo con un total de: $",recaudo2)
else:
    print("La cabina 3 fue la que mas recaudo con un total de: $",recaudo3)

"""

#Ejercicio 20
"""
despegue= Cola()
aterrizaje= Cola()
class Vuelo():
    def __init__(self):
        self.empresa,self.salida,self.llegada,self.origen,self.destino,self.tipo="","","","","",""

print("Agrege los vuelos ordenados por horario de salida: ")
while not cola_llena(c):
    x= Vuelo()
    x.empresa=input("Empresa: ")
    x.salida= input("Horario de salida: ")
    x.llegada= input("Horario de llegada: ")
    x.origen= input("Aeropuerto de origen: ")
    x.destino= input("Aeropuerto destino: ")
    x.tipo= input("Tipo de vuelo: ")
    arribo(despegue,x)



"""
#Ejercicio 21
"""
class Pers():
    def __init__(self):
        self.nombre,self.super,self.genero= "","",""

while not cola_llena(c):
    x= Pers()
    x.nombre=input("Nombre: ")
    x.super= input("Superheroe: ")
    x.genero= input("Genero? F/M: ")
    arribo(c,x)
print("-----------------------------------------------------------")
for i in range(c.tamanio):
    x=Pers()
    x=mover_final(c)
    if x.super== "Capitana Marvel":
        print("El nombre de la Capitana Marvel es: ", x.nombre)

    elif x.nombre== "Scott Lang":
        print("El nombre de superheroe de Scott Lang es: ", x.super)

    elif x.nombre == "Carol Danvers":
        print("Carol Danvers se encuentra en la cola, su nombre de superheroe es: ",x.super)

print("-----------------------------------------------------------")
    
print("Personajes femeninos: ")
for i in range(c.tamanio):
    x=Pers()
    x=mover_final(c)
    if x.genero== "F":
        print(x.nombre)
print("-----------------------------------------------------------")
print("Personajes masculinos: ")
for i in range(c.tamanio):
    x=Pers()
    x=mover_final(c)
    if x.genero== "M":
        print(x.nombre)
print("-----------------------------------------------------------")
print("Personajes/Superheroes cuyos nombres empiezan con s: ")
for i in range(c.tamanio):
    x=Pers()
    x=mover_final(c)
    if x.nombre[0]== "S" or x.super[0]== "S":
        print("Nombre: ",x.nombre)
        print("Superheroe: ",x.super)
        print("Genero: ",x.genero)
"""


from tda_pila import Pila, pila_llena, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint,choice

p = Pila()


#ejercicio 1
"""
cont= 0
while not pila_llena(p):
    a=randint(0,10)
    print(a)
    apilar(p,a)

n=int(input("Ingrese el numero que desea saber cuantas veces se repite: "))

while not pila_vacia(p):
    x=desapilar(p)
    if x == n:
        cont +=1

print("El numero de veces que se repite {} es: {}".format(n,cont))
"""


#ejercicio 2 : 
"""
paux= Pila()
while not pila_llena(p):
    x =int(input("ingrese un numero: "))
    apilar(p,x)

while not pila_vacia(p):
    x = desapilar(p) 
    if x % 2 == 0:   
        apilar(paux,x)

while not pila_vacia(paux):
    x= desapilar(paux)
    apilar(p,x)
   """
"""
#Ejercicio 3
paux= Pila()
while not pila_llena(p):
    a=randint(0,10)
    print(a)
    apilar(p,a)

n=int(input("Ingrese cual es el elemento que desea cambiar: "))
remplazo=int(input("Ingrese por cual desea cambiarlo: "))

while not pila_vacia(p):
    x= desapilar(p)
    if x == n:
        apilar(paux,remplazo)
    else:
        apilar(paux,x)
p=paux

print("La pila con los elementos cambiados puede verse a continuacion: ")

while not pila_vacia(p):
    x=desapilar(p)
    print(x)

"""



#Ejercicio 4
"""
aux = Pila()

while not pila_llena(p):
    x= int(input("Ingrese un numero: "))
    apilar(p,x)

while not pila_vacia(p):
    x= desapilar(p)
    apilar(aux,x)

p = aux

while not pila_vacia(p):
    x=desapilar(p)
    print(x)

"""    

#ejercicio 5
"""

palabra = input("Introduzca una palabra, se evalura si es un palindromo: ")
aux=0

while not aux == len(palabra):
    apilar(p,palabra[aux]) 
    aux+=1

aux=0
while not pila_vacia(p):
    x= desapilar(p)
    if x == palabra[aux]:
        aux+=1

if len(palabra) ==aux:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")
"""

#ejercicio 6
"""
p= Pila()
pal= input("Ingrese una palabra: ")

for i in pal:
    apilar(p,i)

while not pila_vacia(p):
    x= desapilar(p)
    print(x)
"""

#ejercicio 7
"""
aux= Pila()
flag= True
while not pila_llena(p):
    x= randint(1,100)
    print(x)
    apilar(p,x)

elim= int(input("Ingrese el numero del elemento que desea eliminar: "))

while flag and not pila_vacia(p):
    if p.cima == elim:
        desapilar(p)
        flag= False
    else: 
        x= desapilar(p)
        apilar(aux,x)    

while not pila_vacia(aux):
    x=desapilar(aux)
    apilar(p,x)

while not pila_vacia(p):
    x= desapilar(p)
    print(x)
"""

#Ejercicio 8
"""
poro,pespada,pbasto,pcopa,paux,ordenada = Pila(),Pila(),Pila(),Pila(),Pila(),Pila()

class Cartas():
    def __init__(self):
        self.numero,self.palo=0,""

minimo,max= Cartas(),Cartas()

def ordenar(poro,paux,ordenada,minimo):
    if (pila_vacia(poro) and pila_vacia(paux)) or pila_llena(ordenada):
        apilar(ordenada,minimo)
        return "La pila ha sido ordenada"
    else: 
        while not pila_vacia(poro):
            prueba=Cartas()
            prueba=desapilar(poro)
            if minimo.numero > prueba.numero:
                apilar(paux,minimo)
                minimo=prueba
            else:
                apilar(paux,prueba)
        apilar(ordenada,minimo)
        minimo= desapilar(paux)
        return ordenar(paux,poro,ordenada,minimo)
    
palos= ["oro","espada","basto", "copa"]

while not pila_llena(p):
    carta= Cartas()
    carta.numero = randint(1,12)
    carta.palo= choice(palos)
    apilar(p,carta)

while not pila_vacia(p):
    x=desapilar(p)
    if x.palo == "oro":
        apilar(poro,x)
    if x.palo == "espada":
        apilar(pespada,x)
    elif x.palo == "basto":
        apilar(pbasto,x)
    elif x.palo == "copa":
        apilar(pcopa,x)

minimo=desapilar(poro)
print(ordenar(poro,paux,ordenada,minimo))

poro=ordenada
print("////////////////////////////////////////////")
while not pila_vacia(poro):
    x=desapilar(poro)
    print(x.palo,x.numero)
"""

#ejercicio 9
"""
n=int(input("Ingrese del numero que quiere saber el factorial: "))

if n>1:
    for i in range(2,n+1):
        apilar(p,i)

x=1

while not pila_vacia(p):
    j=desapilar(p)
    x *= j

print("El factorial de {} es: {}".format(n,x))
"""
#ejercicio 10
"""
#Numero de elemento de la pila en >= 8 

paux= Pila()
dioses= ["Zeus", "Hera", "Poseidon", "Afrodita", "Ares", "Artemisa", "Apolo"]

for i in dioses:
    apilar(p,i)

n= int(input("Ingrese en que posicion de la lista desea ingresar el nombre de la diosa Atenea: "))

while n != p.cima:
    x= desapilar(p)
    apilar(paux,x)

apilar(p,"Atenea")

while not pila_vacia(paux):
    x=desapilar(paux)
    apilar(p,x)

while not pila_vacia(p):
    x=desapilar(p)
    print(x)

"""

#ejercicio 11
"""

cont=0
letras= "abcdefghijklmnñopqrstuvwxyz"

while not pila_llena(p):
    apilar(p,choice(letras))

while not pila_vacia(p):
    x=desapilar(p)  
    print(x)
    if x == "a" or x=="e" or x =="i" or x == "o" or x== "u":
        cont+=1
    
print("La cantidad de vocales en esta pila es de: {}".format(cont))
"""

#ejercicio 12
"""
paux= Pila()
leia= False
boba= False

personajes= ["Darth Vader", "Chewbacca", "Yoda", "R2-D2", "Luke Skywalker", "C3PO", "Han Solo", "Leia Organa", "Boba Fett"]

while not pila_llena(p):
    apilar(p, choice(personajes))

while not pila_vacia(p):
    x=desapilar(p)
    apilar(paux,x)
    if x == "Leia Organa":
        leia= True
    elif x == "Boba Fett":
        boba= True

while not pila_vacia(paux):
    x=desapilar(paux)
    apilar(p,x)

if leia:
    print("Leia Organa se encuentra en la lista")
if boba:
    print("Boba Fett se encuentra en la lista")

while not pila_vacia(p):
    x=desapilar(p)
    print(x)
"""

#ejercicio 13
"""
paux= Pila()

def ordenamiento(p,paux,n):
    if pila_vacia(p):
        apilar(p,n)
        while not pila_vacia(paux):
            x= desapilar(paux)
            apilar(p,x)
    else:
        n2=desapilar(p)
        if n > n2:
            apilar(p,n2)
            apilar(p,n)
            while not pila_vacia(paux):
                x= desapilar(paux)
                apilar(p,x)
        else:
            apilar(paux,n2)
            return ordenamiento(p,paux,n)


n=int(input("Ingrese un valor a la pila: "))
apilar(p,n)

while not pila_llena(p):
    n=int(input("Ingrese otro valor a la pila: "))
    ordenamiento(p,paux,n)
    
while not pila_vacia(p):
    x= desapilar(p)
    print(x)
"""

#ejercicio 15
"""
ep5 = Pila()
ep7 = Pila()
paux = Pila()

while not pila_llena(ep5):
    x = input('ingrese un nombre de personaje del ep5 ')
    apilar(ep5, x)

while not pila_llena(ep7):
    x = input('ingrese un nombre de personaje del ep7')
    apilar(ep7, x)

print("interseccion")

while(not pila_vacia(ep5)):
    x = desapilar(ep5)
    while(not pila_vacia(ep7)):
        xaux = desapilar(ep7)
        if(x == xaux):
            print(x)
        apilar(paux, xaux)
    while(not pila_vacia(paux)):
        xaux = desapilar(paux)
        apilar(ep7, xaux)
"""

#ejercicio 16
"""
vocales= Pila()
consonantes = Pila()

texto= "La inteligencia artificia1212l (IA) es la inteligenc1235ia llevada a c456abo por máquinas. "

for i in texto:
    if i.isdigit():
        apilar(vocales,i)
    elif i.isalpha():
        apilar(consonantes,i)
    elif i != " ":
        apilar(p,i)

while not pila_vacia(vocales):
    x=desapilar(vocales)
    print(x)


#ejercicio 17
"""
x = []
paux= Pila()
ordenada= Pila()

def ordenar(p,paux,ordenada,min,max):
    if pila_llena(ordenada):
        return "La pila ha sido ordenada"
    else: 
        while not pila_vacia(p):
            prueba=desapilar(p)
            if min[1] > prueba[1]:
                apilar(paux,min)
                min=prueba
            else:
                if max[1] < prueba[1]:
                    max=prueba
                apilar(paux,prueba)
        apilar(ordenada,min)
        return ordenar(paux,p,ordenada,max,min)

while not pila_llena(p):   
    i= input("Ingrese el nombre del objeto: ")
    j = float(input("Ingrese el peso de {} : ".format(i)))
    x = [i,j]
    apilar(p,x)

min = desapilar(p)
max=min

print(ordenar(p,paux,ordenada,min,max))

max=desapilar(ordenada)
print("El peso maximo es:",max)

print(max)
while not pila_vacia(ordenada):
    x=desapilar(ordenada)
    print(x)
print("Peso minimo: ",x)

#ejercicio 18
"""
class Peliculas():
    def __initi__(self):
        self.titulo,self.estudio,self.anio="","",0
    
marvel= Pila()
cont=0
while not pila_llena(p):
    peli = Peliculas()
    peli.titulo=input("Ingrese el nombre de la pelicula: ")
    peli.estudio=input("Ingrese el estudio que la hizo: ")
    peli.anio=int(input("Igrese el año en que se estreno: "))
    apilar(p,peli)

print("Nombre de peliculas que se estrenaron en 2014: ")
while not pila_vacia(p):
    peli = Peliculas()
    peli= desapilar(p)
    if peli.anio == 2014:
        print(peli.titulo)

    elif peli.anio == 2018:
        cont+=1

    elif peli.anio == 2016 and peli.estudio == "Marvel Studios":
        apilar(marvel,peli)

print ("El numero de peliculas estrenadas en 2018 es: {}".format(cont))
print("Peliculas de marvel el año 2016: ")

while not pila_vacia(marvel):
    peli = Peliculas()
    peli= desapilar(marvel)
    print(peli.titulo)
"""

#ejercicio 19
"""

class robot():
    def __init__(self):
        self.pasos, self.direccion= 0, ""

def volver(x):
    global inv
    if x.direccion=="sur":
        inv="norte"
    elif x.direccion=="norte":
        inv="sur"
    elif x.direccion=="este":
        inv="oeste"
    elif x.direccion=="oeste":
        inv="este"
    elif x.direccion=="sureste":
        inv="noroeste"
    elif x.direccion=="noreste":
        inv="suroeste"
    elif x.direccion=="suroeste":
        inv="noreste"
    elif x.direccion=="noroeste":
        inv="sureste"

while not pila_llena(p):
    r=robot()
    r.pasos=int(input("Cantidad de pasos: "))
    r.direccion=input("Direccion: ")
    apilar(p,r)

while not pila_vacia(p):
    x=desapilar(p)
    volver(x)
    print(x.pasos,inv)
"""


#ejercicio 20
"""
apilar(p,0)
apilar(p,1)
cont=2
num = int(input("Ingrese hasta que numero quiere realizar la sucesion de Fibonacci: "))

while cont < num:
    x= desapilar(p)
    j = desapilar(p)
    suces = x + j
    apilar(p,j)
    apilar(p,x)
    apilar(p,suces)
    cont+=1

while not pila_vacia(p):
    j=desapilar(p)
    print(j)
""" 
#ejercicio 21 
"""
media,encima,debajo= 0, 0, 0
paux= Pila()


while not pila_llena(p):
    x= int(input("Ingrese la temperatura del dia {}: ".format(p.cima+2)))
    apilar(p,x)
    media+=x

minimo,maximo = x,x
media= media//(p.cima+1)



while not pila_vacia(p):
    x=desapilar(p)
    apilar(paux,x)
    if x > maximo:
        maximo=x
    if x < minimo:
        minimo=x
    if x < media:
        debajo+=1
    if x > media:
        encima+=1

print("El mes de abril tuvo una minima de {}° y una maxima de {}°".format(minimo,maximo))
print("La media de temperatura fue: {}°".format(media) )
print("Teniendo {} dias por debajo y {} dias por encima de la media ".format(debajo,encima))

while not pila_vacia(paux):
    x=desapilar(paux)
    apilar(p,x)
"""

#ejercicio 22
"""
paux= Pila()
rocket, groot=0,0
class Personaje():
    def __init__(self):
        self.nombre,self.peliculas="",0

while not pila_llena(p):
    personajes= Personaje()
    personajes.nombre= input("Ingrese el nombre del personaje de Marvel: ")
    personajes.peliculas=int(input("En cuantas peliculas de la saga participo?: "))
    apilar(p,personajes)
cont=0

while not pila_vacia(p):
    cont+=1
    personajes= Personaje()
    personajes=desapilar(p)
    if personajes.nombre == "Rocket Raccoon":
        rocket=cont
    elif personajes.nombre == "Groot":
        groot= cont
    elif personajes.nombre == "Black Widow":
        print("Black Widow participo en {} peliculas".format(personajes.peliculas))

    if personajes.peliculas > 5:
        apilar(paux,personajes)

    if personajes.nombre[0] == "C" or personajes.nombre[0] == "D" or personajes.nombre[0] == "G": 
        print(personajes.nombre)

if rocket != 0:
    print("Rocket Raccoon aparece en la posicion: ",rocket)

if groot !=0:
    print ("Groot aparece en la posicion: ",groot)

print("Personajes que participaron en mas de 5 peliculas: ")

while not pila_vacia(paux):
    personajes= Personaje()
    personajes=desapilar(paux)
    print("{} participo en {} peliculas".format(personajes.nombre,personajes.peliculas))
"""
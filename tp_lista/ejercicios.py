from tda_lista import Lista, insertar, eliminar,busqueda,barrido, tamanio, lista_vacia, nodoLista
from random import randint
from tda_lista_lista import Lista, insertar, eliminar, busqueda, barrido, barrido_con_sublista, tamanio, lista_vacia, criterio
import time

lista= Lista()
aux= Lista()

# Ejercicio 1
"""
for i in range(15):
    insertar(lista, randint(0,50))
c= 0

aux=lista.inicio

while(aux is not None):
    c+=1
    aux = aux.sig

print(c)
"""
#Ejercicio 2
"""
for i in range(15):
    insertar(lista, chr(randint(65,90)))

barrido(lista)

dato = eliminar(lista, 'A')
while(dato is not None):
    dato = eliminar(lista, 'A')

dato = eliminar(lista, 'E')
while(dato is not None):
    dato = eliminar(lista, 'E')

dato = eliminar(lista, 'I')
while(dato is not None):
    dato = eliminar(lista, 'I')

dato = eliminar(lista, 'O')
while(dato is not None):
    dato = eliminar(lista, 'O')

dato = eliminar(lista, 'U')
while(dato is not None):
    dato = eliminar(lista, 'U')

print()
barrido(lista)
"""

#Ejercicio 3
"""
par= Lista()
impar= Lista()

for i in range(15):
    insertar(lista, randint(1,100))

barrido(lista)

while not lista_vacia(lista):
    dato= eliminar(lista, lista.inicio.info)
    if dato % 2 == 0:
        insertar(par,dato)
    else:
        insertar(impar, dato)

print("Lista par: ")
barrido(par) 

print("Lista impar: ")
barrido(impar)

barrido(lista)
"""
# Ejercicio 4
"""
aux2= Lista()
aux3=nodoLista()
for i in range(15):
    insertar(lista, randint(0,50))

barrido(lista)

ins=int(input("Ingrese la posicion en la que desea insertar el dato: "))
num=int(input("Ingrese el dato que desea agregar a la lista: "))
cont=0
aux= lista.inicio
aux2= aux
aux3.info=num
if ins == 0:
    lista.inicio=aux3
    aux3.sig=aux
else:
    while cont < ins-1:
        aux= aux.sig
        aux2= aux2.sig
        cont+=1   
    aux2=aux2.sig
    aux.sig= aux3
    aux3.sig=aux2

barrido(lista)
"""
#Ejercicio 5
"""
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

for i in range(15):
    insertar(lista, randint(1,100))

barrido(lista)
aux= lista.inicio
while aux is not None:
    if isPrime(aux.info):
        eliminar(lista, aux.info)
        aux= aux.sig
    else:
        aux= aux.sig

print("Lista sin primos: ")
barrido(lista)
"""
#Ejercicio 6

"""

class Superheroes():
    def __init__(self):
        self.nombre,self.anio,self.casa,self.biografia= "",0,"",""

def eliminarpers(lista, clave):
    dato = None
    if(lista.inicio.info.nombre == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and act.info != clave):
            act = act.sig
            ant = ant.sig
        
        if(act is not None):
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1

    return dato

def barridoheroes(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info.nombre,",",aux.info.anio,",",aux.info.casa,",",aux.info.biografia)
        aux = aux.sig

for i in range(5):
    x= Superheroes()
    x.nombre= input("Nombre: ")
    x.anio= int(input("Año: "))
    x.casa=input("Casa [Marvel/DC]: ")
    x.biografia=input("Biografia: ")
    insertar(lista, x)

barridoheroes(lista)
eliminarpers(lista, "Linterna Verde")

barridoheroes(lista)

"""
#Ejercicio 7

"""

class marvel():
    def __init__(self, nombre, año, casa_comic, biografia):
        self.nombre,self.año,self.casa_comic,self.biografia = "",0,"",""

def str(self):
    return self.nombre + " " +str(self.año) + " " + self.casa_comic + " " + self.biografia

com_bms = []
sh1963 = []
sh_traje_armadura = []
lista=Lista()
cmarvel=0
cdc=0
letras=["b","m","s"]

for i in range(1):
    nombre=input("Nombre: ")
    año=int(input("Año: "))
    casa_comic=input("Casa de comic: ")
    biografia=input("Biografia: ")
    m=marvel(nombre,año,casa_comic,biografia)
    insertar(lista,m,"nombre")

aux=lista.inicio

while aux is not None:
    dato=eliminar(lista,"linterna verde","nombre")
    print(dato)
    if dato is not None:
        lintverde=True
    else:
        lintverde=False
    
    dato=None

    dato=busqueda(lista,"wolverine","nombre")
    if dato is not None:
        print(dato.info)
    else:
        wolverine=False
    
    dato=None

    dato= busqueda(lista,"dr strange","nombre")
    if dato is not None:
        dato.info.casa_comic="marvel"
    
    dato=None

    if aux.info.año<1963:
        sh1963.append(aux.info)

    dato=busqueda(lista,"capitana marvel","nombre")
    if dato is not None:
        print("Capitana marvel pertenece a la casa de comic ",dato.info.casa_comic)

    dato=None

    dato=busqueda(lista,"mujer maravilla","nombre")
    if dato is not None:
        print("Mujer maravilla peretenece a la casa de comic ",dato.info.casa_comic)
    
    dato=None

    dato=busqueda(lista,"flash","nombre")
    if dato is not None:
        print("Informacion de Flash: ",dato.info)
    
    dato=None
    dato=busqueda(lista,"star lord","nombre")
    if dato is not None:
        print("informacion de Star Lord: ", dato.info)
    
    if ((aux.info.nombre)[0] == 'B'):
        com_bms.append(aux.info)

    if (criterio(aux.info.nombre, 'nombre'[0]) == 'M'):
        com_bms.append(aux.info)

    if (criterio(aux.info.nombre, 'nombre')[0:len('S')] == 'S'):
        com_bms.append(aux.info)
    
    if ((aux.info.biografia.find("traje")) != -1 or (aux.info.biografia.find("armadura") != -1 )):
        sh_traje_armadura.append(aux.info.nombre)
    
    if aux.info.casa_comic=="marvel":
        cmarvel+=1
    else:
        cdc+=1
    
    aux=aux.sig
if lintverde:
    print("Linterna verde se elimino correctamente")
else:
    print("No se encontro a Linterna Verde")

if not wolverine:
    print("No se encontro a Wolverine")

print("Superherores cuya fecha de aparicion sea anterior a 1963: ")
print(sh1963)

print("Cantidad de superheroes de marvel: ",cmarvel)
print("Cantidad de superheroes de DC: ",cdc)

print("Superheroes que empiezan con B, M o S: ")
for i in range (len(com_bms)):
    print(str(com_bms[i]))
"""
#Ejercicio 9
"""
lista=Lista()

class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre, self.apellido, self.legajo = "","",""
    
    def __str__(self):
        return self.apellido + " " + self.nombre

class Parcial(object):
    
    def __init__(self, materia, nota, fecha):
        self.materia, self.nota , self.fecha = "", 0, ""

    def __str__(self):
        return self.materia + " " + self.nota
    

for i in range(10):
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    legajo=input("Legajo: ")
    Alumno(nombre,apellido,legajo)
    insertar(lista,Alumno,"apellido")

legajo = input('Ingrese legajo ')
while(legajo != ''):
    pos = busqueda(lista, legajo, 'legajo')
    if(pos is not None):
        materia = input('Ingrese materia ')
        nota = int(input('Ingrese nota: '))
        fecha = ''#input('ingrese fecha')
        parcial = Parcial(materia, nota, fecha)
        insertar(pos.sublista, parcial, 'materia')

    legajo = input('Ingrese legajo ')

    # * punto A
barrido(lista)

# * punto B, C, D, E
aux = lista.inicio
while(aux is not None):
    promedio = 0
    parciales = aux.sublista.inicio
    control = True
    while(parciales is not None):
        if(parciales.info.nota < 6):
            control = False
        promedio += parciales.info.nota
        parciales = parciales.sig
        
    
    if(control and tamanio(aux.sublista) > 0):
        print('aprobo todos los examenes', aux.info)

    if(tamanio(aux.sublista) > 0 ):
        promedio = promedio / tamanio(aux.sublista) 
    print(promedio, aux.info)
    if(promedio>8.89):
        print('promedio mayor a ..', aux.info, promedio)

    if(aux.info.apellido[0].upper() == 'L'):
        print('comienza con..', aux.info)


    aux = aux.sig
"""
#Ejercicio 10
"""
lista=Lista()
arctic=[]
banda_palabra = []
maxd=0


class Cancion():
    def __init__(self):
        self.nombre, self.banda, self.duracion, self.reproducciones = "","",0,0

def mostrar(c):
    return c.nombre + " " +c.banda + " " + str(c.duracion) + " " + str(c.reproducciones)


for i in range(3):
    c= Cancion()
    c.nombre = input("Nombre: ")
    c.banda = input("Banda o Artista: ")
    c.duracion = int(input("Duracion: "))
    c.reproducciones = int(input("Reproducciones: "))
    insertar(lista, c, "nombre")

aux=lista.inicio
maxinfo=Cancion()
while aux is not None:

    if aux.info.duracion>maxd:
        maxd = aux.info.duracion
        maxinfo = aux.info

    if aux.info.banda == "arctic monkeys":
        arctic.append(aux.info.nombre)

    if aux.info.banda.find(" ") == -1:
        banda_palabra.append(aux.info.banda)
    aux=aux.sig


print("Canciones de Arctic Monkeys: ")
for i in range(len(arctic)):
    print(str(arctic[i]))

print("Bandas o artistas de una sola palabra: ", banda_palabra)

print("Info. de la cancion mas larga: ",mostrar(maxinfo))
"""
#Ejercicio 11

"""perfem=[]
per850=[]
droide=[]
mayor850=0

class Starwars:
    def __init__(self, nombre, altura, edad, genero, especie, planeta, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodios = episodios

    def __str__(self):
        return self.nombre + " " +str(self.altura) + " " + str(self.edad) + " " +self.genero + " " + self.especie + " " + self.planeta + " " + str(self.episodios)

print("Personajes de Star Wars: ")

for i in range(1):
    nombre=input("Nombre: ")
    altura=int(input("Altura: "))
    edad=int(input("Edad: "))
    genero=input("Genero: ")
    especie=input("Especie: ")
    planeta=input("Planeta: ")
    episodios=0
    stw=Starwars(nombre, altura, edad, genero, especie, planeta, episodios)
    insertar(lista,stw,"nombre")

personaje=input("Personaje: ")
while (personaje!=""):
    pos=busqueda(lista, personaje, "nombre")
    if pos is not None:
        cap=int(input("Capitulos en los que aparece: "))
        insertar(pos.sublista, cap, "episodios")
    
    personaje=input("Personaje: ")


aux=lista.inicio

while aux is not None:
    if aux.info.genero=="femenino":
        perfem.append(aux.info.nombre)
    
    if (aux.info.especie=="droide" and aux.info.episodios>=1 and aux.info.episodios<=6):
        droide.append(aux.info.nombre)
    
    if (aux.info.nombre=="darth vader") or (aux.info.nombre=="han solo"):
        print(aux.info)
    
    if aux.info.edad>850:
        per850.append(aux.info.nombre)
        if aux.info.edad>mayor850:
            mayor850=aux.info.edad
            permayor850=aux.info.nombre
    
    dato=eliminar(lista,4,episodios)
    dato=eliminar(lista,5,episodios)
    dato=eliminar(lista,6,episodios)
    
    aux=aux.sig


print("Personajes de genero femenino: ")
for i in range(len(perfem)):
    print(perfem[i])

print("Personajes de especie droide que aparecieron en los primeros seis episodios de la saga: ")
for i in range(len(droide)):
    print(droide[i])

print("Personajes mayores a 850 años: ")
for i in range(len(per850)):
    print (per850[i])

print("De ellos el mayor es ",permayor850)"""

#Ejercicio 15

lista=Lista()
torngan3=[]
entr79=[]
cantentr=0
entrpokdet=[]
class Entrenador():
    def __init__(self):
        self.nombre, self.torneosgan,self.batperd,self.batgan,self.pokemon = "",0,0,0, Pokemon

class Pokemon():
    def __init__(self):
        self.nombre,self.nivel,self.tipo,self.subtipo="",0,"",""

print("Entrenadores Pokemon")
for i in range(2):
    entren= Entrenador()
    entren.nombre=input("Nombre: ")
    entren.torneosgan=int(input("Torneos ganados: "))
    entren.batperd=int(input("Batallas perdidas: "))
    entren.batgan=int(input("Batallas ganadas: "))
    insertar(lista, entren, "nombre")

entrenador=input("Entrenador: ")
while entrenador!="":
    dato=busqueda(lista,entrenador,"nombre")
    res="si"
    if dato is not None:
        while res=="si":
            pkmn= Pokemon()
            pkmn.nombre=input("Nombre: ")
            pkmn.nivel=int(input("Nivel: "))
            pkmn.tipo=input("Tipo: ")
            pkmn.subtipo=input("Subtipo: ")
            insertar(dato.sublista, pkmn, "pokemon")
            res=input("Desea cargar mas? si/no")
    entrenador= input("Ingrese otro entrenador o vacio: ")

aux=lista.inicio
while aux is not None:
    if aux.info.torneosgan>3:
        torngan3.append(aux.info.torneosgan)
    
    if aux.info.pokemon.nivel>maxnivel and aux.info.torneosgan>maxtganados:
        maxnivel=aux.info.pokemon.nivel
        maxtganados=aux.info.maxtganados

    entrbusq=input("Ingrese el entrenador del cual desea obtener su info.: ")
    dato = busqueda(lista, entrbusq,"nombre")
    if dato is not None:
        print(aux.info)
    
    if aux.info.batgan/(aux.info.batgan + aux.info.batperd)*100>79:
        entr79.append(aux.info.nombre)
    
    entrbusq=input("Ingrese el entrenador del cual desea saber el promedio de nivel de sus Pokemons: ")
    dato = busqueda(lista,entrbusq,"nombre")
    if dato is not None:
        for i in range(tamanio(dato.sublista)):
            acunivel = aux.info.pokemon.nivel + acunivel
        
        prom = acunivel/tamanio(dato.sublista)
        print("Promedio: ",prom)

    pokbusq = input("Ingrese el pokemon que desea saber cuantos entrenadores lo tienen: ")
    if aux.info.pokemon.nombre == pokbusq:
        cantentr+=1

    if aux.info.pokemon.nombre in ["tyrantrum", "terrakion", "wingull"]:
        entrpokdet.append(aux.info.nombre)

#Ejercicio 16

"""atiempo=[]
adestiempo=[]
infofechas=[]
actividades=[]
costototal=0
acutiempo=0


class Proyecto:
    def __init__(self, actividad, costo, tiempo_ejecucion, fecha_inicio, fecha_fin_est, fecha_final, encargado):
        self.actividad = actividad
        self.costo = costo
        self.tiempo_ejecucion = tiempo_ejecucion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_est = fecha_fin_est
        self.fecha_final = fecha_final
        self.encargado = encargado
    
    def __str__(self):
        return str(self.costo) + str(self.tiempo_ejecucion) + self.fecha_inicio + self.fecha_fin_est + self.fecha_final + self.encargado
    
for i in range(1):
    actividad = input("Actividad: ")
    costo = int(input("Costo: "))
    tiempo_ejecucion = int(input("Tiempo de ejecucion: "))
    fecha_inicio = input("Fecha de inicio: ")
    fecha_fin_est = input("Fecha final estimada: ")
    fecha_final = input("Fecha final efectiva: ")
    encargado = input("Persona a cargo: ")
    p = Proyecto(actividad, costo, tiempo_ejecucion, fecha_inicio, fecha_fin_est, fecha_final, encargado)
    insertar(lista, p, "actividad")

aux = lista.inicio
persona = input("Ingrese la persona que desea saber que tarea hizo: ")
fecha_base = input("Ingrese a partir de que fecha desea obtener informacion: ")
fecha_tope = input("Fecha tope: ")
while aux is not None:
    acutiempo = acutiempo + aux.info.tiempo_ejecucion
    costototal = costototal + aux.info.costo

    dato = busqueda(lista, persona, "encargado")
    if dato is not None:
        actividades.append(aux.info.actividad)
    
    if (aux.info.fecha_inicio >= fecha_base) and (aux.info.fecha_final <= fecha_tope):
        infofechas.append(aux.info)
    
    if fecha_fin_est <= fecha_final:
        atiempo.append(aux.info.actividad)
    else:
        adestiempo.append(aux.info.actividad)
    
    aux = aux.sig

print("Costo total del proyecto: ",costototal)
print("Tiempo promedio de tareas: ",acutiempo/lista.tamanio)

print("Actividades relizadas por ",persona," :")
for i in range(len(actividades)):
    print(actividades[i])

print("Informacion de actividades entre dos fechas: ")
for i in range(len(infofechas)):
    print(infofechas[i])

print("Actividades terminadas a tiempo: ")
for i in range(len(atiempo)):
    print(atiempo[i])

print("Actividades terminadas fuera de tiempo: ")
for i in range(len(adestiempo)):
    print(adestiempo[i])"""
#Ejercicio 17

"""infodestinos = []
turistadispo = []
vuelos_fecha = []
vuelos_tailandia = []

class Vuelo():
    def __init__(self, empresa, nro_vuelo, cant_asientos_total, asientos_1c, asientos_ocu_1c, asientos_turi, asientos_ocu_turi, fecha_salida, destino, kms):
        self.empresa = empresa
        self.nro_vuelo = nro_vuelo
        self.cant_asientos_total = cant_asientos_total
        self.asientos_1c = asientos_1c
        self.asientos_ocu_1c = asientos_ocu_1c
        self.asientos_turi = asientos_turi
        self.asientos_ocu_turi = asientos_ocu_turi
        self.fecha_salida = fecha_salida
        self.destino = destino
        self.kms = kms


    def __str__(self):
        return self.empresa + str(self.nro_vuelo) + str(self.cant_asientos_total) + str(self.asientos_1c) + str(self.asientos_ocu_1c) + str(self.asientos_turi) + str(self.asientos_ocu_turi) + self.fecha_salida + self.destino + str(self.kms)
    

for i in range(1):
    empresa = input("Empresa: ")
    nro_vuelo = int(input("Numero de vuelo: "))
    cant_asientos_total = int(input("Cantidad de asientos totales: "))
    asientos_1c = int(input("Cantidad de asientos de primera clase: "))
    asientos_ocu_1c = int(input("Cantidad de asientos ocupados de primera clase: "))
    asientos_turi = int(input("Cantidad de asientos de clase turista: "))
    asientos_ocu_turi = int(input("Cantidad de asientos ocupados de clase turista: "))
    fecha_salida = input("Fecha de salida: ")
    destino = input("Destino: ")
    kms = input("Kilometros: ")
    v = Vuelo (empresa, nro_vuelo, cant_asientos_total, asientos_1c, asientos_ocu_1c, asientos_turi, asientos_ocu_turi, fecha_salida, destino, kms)
    insertar(lista, v, "empresa")

aux = lista.inicio
fecha = input("Ingrese la fecha para la que desea saber los vuelos programados: ")
elim_vuelo = int(input("Ingrese el nro de vuelo que desea eliminar: "))

while aux is not None:

    if aux.info.destino in ["atenas", "miconos", "rodas"]:
        infodestinos.append(aux.info)
    
    if aux.info.asientos_ocu_turi < aux.info.asientos_turi:
        turistadispo.append(aux.info.nro_vuelo)
    

    print("El vuelo ", aux.info.nro_vuelo, " recaudo $", (aux.info.asientos_ocu_1c*kms*203) + (aux.info.asientos_ocu_turi*kms*75))
    
    dato = busqueda(lista, fecha, "fecha_salida")
    if dato is not None:
        vuelos_fecha.append(aux.info.nro_vuelo)
    
    dato = eliminar(lista, elim_vuelo, "nro_vuelo")
    if dato is not None:
        print("La empresa debe devolver $",(aux.info.asientos_ocu_1c*kms*203) + (aux.info.asientos_ocu_turi*kms*75), " por cancelar el vuelo ", elim_vuelo)
    
    if aux.info.destino == "tailandia":
        vuelos_tailandia.append(aux.info.empresa, aux.info.kms)
    
    aux = aux.sig

print("Vuelos con destino a Atenas, Miconos o Rodas: ", infodestinos)

print("Vuelos con asientos clase turista disponibles: ", turistadispo)

print("Vuelos con destino a Tailandia: ", vuelos_tailandia)"""


#Ejercicio 18
"""
class Comit():
    def __init__(self):
        self.timestap,self.mensaje,self.archivo,self.lineas="","","",0

class Colaboradores():
    def __init__(self):
        self.nombre,self.comit= "", Comit()

def mostrar(self):
        return self.timestap + " " + self.mensaje + " " + self.archivo + " " + str(self.lineas)

print("Cargar usuarios: ")

for i in range(1):
    user= Colaboradores()
    user.nombre= input("Nombre: ")
    insertar(lista,user, "nombre")

user= input("De que usuario desea agregar un comit?: ")

while user!="":
    dato= busqueda(lista, user, "nombre")
    res="si"
    if dato is not None:
        while res=="si":
            c= Comit()
            c.timestap= input("En que fecha y hora se agrego el comit? : ")
            c.mensaje= input("Mensaje: ")
            c.archivo= input("Archivo: ")
            c.lineas= int(input("Lineas: "))
            insertar(dato.sublista, c, "timestap")
            res= input("Quiere agregar otro comit?: ")
    user=input("Ingrese otro nombre o vacio: ")


mayor=0

aux = lista.inicio
while(aux is not None):
    if(tamanio(aux.sublista) > mayor):
        mayor = tamanio(aux.sublista)
    aux = aux.sig

aux = lista.inicio

print("Maximos: ")
while(aux is not None):
    if(tamanio(aux.sublista) == mayor):
        print(aux.info.nombre)
    aux = aux.sig

max=0
aux = lista.inicio
while aux is not None:
    sublista=aux.sublista.inicio
    max_usuario=0
    while sublista is not None:
        max_usuario+= sublista.info.lineas
        sublista=sublista.sig
    if max_usuario>max:
        max=max_usuario
        usermaximo=aux.info.nombre
    aux=aux.sig


aux=lista.inicio
while aux is not None:
    sublista=aux.sublista.inicio
    flag= False
    while sublista is not None:
        if sublista.info.archivo=="test.py" and sublista.info.timestap[8:13] > "19:45" and not flag:
            print(aux.info.nombre)
            flag= True
        sublista=sublista.sig
    aux=aux.sig

aux=lista.inicio
while aux is not None:
    sublista=aux.sublista.inicio
    while sublista is not None:
        if sublista.info.lineas == 0:
            print(aux.info.nombre)
        sublista=sublista.sig
    aux=aux.sig

fechamax=""
horamax=""
usuariomaximo=""
usermaximo=Comit()
aux=lista.inicio
while aux is not None:
    sublista=aux.sublista.inicio
    flag= False
    while sublista is not None:
        if ((sublista.info.archivo=="app.py") and (sublista.info.timestap[0:7]>=fechamax)):
            if sublista.info.timestap[0:7]==fechamax:
                if sublista.info.timestap[9:13] > horamax:
                    usermaximo=sublista.info
                    usuariomaximo=aux.info.nombre
                    fechamax=sublista.info.timestap[0:7]
                    horamax=sublista.info.timestap[9:13]
            else:
                horamax=""
                usermaximo=sublista.info
                usuariomaximo=aux.info.nombre
                fechamax=sublista.info.timestap[0:7]
                horamax=sublista.info.timestap[9:13]
        sublista=sublista.sig
    aux=aux.sig

print("del usuario que realizó el último commit sobre el archivo app.py es: ",usuariomaximo)
print("Fecha:", usermaximo.timestap)
print("Mensaje:", usermaximo.mensaje)
print("Lineas agregadas:", usermaximo.agregadas)
"""

#Ejericio 19
"""
archivo= open("datos.txt")

cont=0
linea = archivo.read()

for i in range(20):
    
    while not flag:
        if linea[posf]!= ";":
            posf+=1
        else:
            flag= True
            vect.append(linea[posi:posf])
            posf+=2
            posi=posf  

for i in range(len(vect)):
    print(vect[i])
posi=0
posf=0
vect=[]
archivo = open('datos.txt')
linea = archivo.readline()
print('archivo')
while linea:
    linea = linea.replace('\n', '')
    for i in range(4):
        flag=False
        while not flag:
            if linea[posf]!= ";":
                posf+=1
            else:
                flag= True
                vect.append(linea[posi:posf])
                posf+=2
                posi=posf 
    print(linea)
    linea = archivo.readline()
"""

#Ejercicio 20 
"""
class Clima():
    def __init__(self):
        self.temperatura,self.presion,self.humedad,self.estadoclima,self.fecha,self.hora= 0,0,0,"","",""

class Estaciones():
    def __init__(self):
        self.nombre,self.pais,self.latitud,self.longuitud,self.altitud,self.clima="", "",0,0,0,Clima()

def Mostrar(m):
    return m.nombre+" "+ m.pais+" "+str(m.latitud)+" "+str(m.longuitud)+" "+str(m.altitud)

for i in range(2):
    estacion= Estaciones()  
    estacion.nombre=input("Nombre: ")
    estacion.pais= input("Pais: ")
    estacion.latitud= int(input("Latitud: "))
    estacion.longuitud= int(input("Longuitud: "))
    estacion.altitud= int(input("Altitud: "))
    insertar(lista,estacion, "pais")

nombre= ("Nombre de la persona que ingreso la estacion:")
while nombre !="":
    res="si"
    dato= busqueda(lista, nombre, "nombre")
    while res=="si"
        if dato is not None:
            c= Clima()
            c.temperatura= int(input("Ingrese la temperatura: "))
            c.presion= int(input("Ingrese presion: "))
            c.humedad= int(input("Ingrese humedad: "))
            c.estadoclima= input("Ingrese el estado del clima: ")
            c.fecha= input("Fecha: ")
            c.hora= input("Hora: ")
            insertar(dato.sublista, c, "estadoclima")
        res= input("Desea cargar otra estacion?: ")
    nombre= input("Ingrese otro nombre o vacio: ")

aux= lista.inicio
actemp=0
achum=0
cont=0
while aux is not None:
    sublista=aux.sublista.inicio
    while sublista is not None:
        if sublista.info.fecha[3:5] == "05":
            cont+=1
            actemp+=sublista.info.temperatura
            achum+=sublista.info.humedad
        sublista=sublista.sig
    aux=aux.sig

if cont !=0:
    print("Promedio de humedad en mes de mayo: ",achum/cont)
    print("Promedio de temperatura en mes de mayo: ",actemp/cont)

time.strftime("%d/%m/%Y")
aux= lista.inicio
while aux is not None:
    sublista=aux.sublista.inicio
    while sublista is not None:
        if sublista.info.fecha == time.strftime("%d/%m/%Y"):
            if sublista.info.estadoclima == "lloviendo" or sublista.info.estadoclima == "nevando":
                print("En ",aux.info.pais," hoy esta ",sublista.info.estadoclima)
        sublista=sublista.sig
    aux=aux.sig

aux= lista.inicio
print("Se presentaron tormentas electricas o huracanes en: ")
while aux is not None:
    flag= False
    sublista=aux.sublista.inicio
    while sublista is not None:
        if sublista.info.estadoclima == "tormenta electrica" or sublista.info.estadoclima == "huracanes" and not flag:
                flag= True
        sublista=sublista.sig
    if flag:
        print(Mostrar(aux.info))
    aux=aux.sig

"""


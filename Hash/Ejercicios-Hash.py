import tda_hash
import tdaListaLista
from random import choice, randint
#Ejercicio 1
"""
class Palabra(object):

    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
    
    def __str__(self):
        return self.palabra

tabla = crear_tabla(26)



tabla = crear_tabla(26)
# punto A
palabra = Palabra('hola', 'es un saludo')
agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
palabra = Palabra('hielo', 'agua congelada')
agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
palabra = Palabra('arbol', 'asdasdsadsda')
agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
for i in tabla:
    if(i is not None):
        barrido(i)
print()
# punto B
pos = buscar_ta(tabla, hash_diccionario, Palabra('hola',''), 'palabra')
if(pos is not None):
    print('palabra', pos.info.palabra, 'significado', pos.info.significado)
print()
#punto C
print('elemento eliminado', quitar_ta(tabla, hash_diccionario, Palabra('hielo',''), 'palabra'))
for i in tabla:
    if(i is not None):
        barrido(i)
"""
#Ejercicio 2

"""tabla = crear_tabla(20)

class Guia():
    def __init__(self, nro, apellido, nombre, direccion):
        self.nro = nro
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    
    def _str_(self):
        return str(self.nro) + self.apellido + self.nombre

def hash_division_telefono(Guia, tabla):
    return Guia.nro % len(tabla)

for i in range(3):
    nro = int(input("Numero de telefono: "))
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    direccion = input("Direccion: ")
    g = Guia(nro, apellido, nombre, direccion)
    agregar_ta(tabla, hash_division_telefono, g, "nro")"""

#Ejercicio 4

"""tabla = crear_tabla(20)
profesores = crear_tabla(20)

class Catedra():
    def __init__(self, codigo, nombre, modalidad, horas):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.horas = horas
        self.docentes = docentes
    
    def __str__(self):
        return str(self.codigo) + self.nombre + self.modalidad + str(self.horas)

def hash_division_catedras(Catedra, tabla):
    return Catedra.codigo % len(tabla)



print("Catedra")
for i in range(3):
    codigo = int(input("Codigo: "))
    nombre = input("Nombre: ")
    modalidad = input("Modalidad: ")
    horas = int(input("Horas: "))
    docentes = ""
    c = Catedra(codigo, nombre, modalidad, horas)
    agregar_tc(tabla, hash_division_catedras, c)

cod = input("Codigo: ")
dato = buscar_tc(tabla, hash_division_catedras, cod)
if dato is not None:
    cant = int(input("Ingrese cuantos docentes desea cargar: "))
    for i in range(cant):
        prof = input("Docente: ")
        agregar_tc(docentes, hash_division_catedras, prof)"""


#Ejercicio 4

"""tabla = crear_tabla(3)

for i in range(3):
    personaje = input("Personaje: ")
    agregar_tc(tabla, bernstein, personaje)

for i in range(cantidad_elementos_tc(tabla)):
    print(tabla[i])
"""
#Ejercicio 6
"""
letras = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legion = crear_tabla(10)
tabla_codigos = crear_tabla(1000)

class Stormtrooper(object):

    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo
    
    def __str__(self):
        return self.legion+' '+str(self.codigo)

for i in range(1,2000):
    legion = choice(letras)
    codigo = randint(1000, 9999)
    trooper = Stormtrooper(legion, codigo)
    agregar_ta(tabla_legion, bernstein_troopers, trooper, 'legion')
    agregar_ta(tabla_codigos, hash_division_troopers, trooper, 'codigo')


posicion = bernstein('FN', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = bernstein('CT', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = hash_division(537, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])
print()
posicion = hash_division(781, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])"""

#Ejercicio 8

"""tabla = crear_tabla(10)
tabla2 = crear_tabla(10)
cadena_encriptada = ""
msj_descifrado=""

def encriptar(cadena):
    global cadena_encriptada
    for i in range(len(cadena)):
        caracter = cadena[i]
        caracter_ascii = str(ord(caracter)+10000000)
        cadena_encriptada = cadena_encriptada + caracter_ascii
    return cadena_encriptada

def desencriptar(dato):
    global msj_descifrado
    for i in range(0, len(dato),8):
        cod = dato[i:i+8]
        cod = int(cod) - 10000000
        msj_descifrado += chr(cod)
    return msj_descifrado


cadena= input("Ingrese una cadena: ")
print(encriptar(cadena))

dato = input("Ingrese el mensaje cifrado: ")
desencriptar(dato)
print(msj_descifrado)
"""

#Ejercicio 9
"""tabla = crear_tabla(10)

dic=["#?&","abc", "def", "ghi", "jkl", "mnñ", "opq", "rst", "uvw", "xyz"]


def cifrar(cadena):
    cifrado=""
    for i in range(len(cadena)):
        caracter = str(ord(cadena[i]))
        for j in caracter:
            num = int(j)
            cifrado += dic[num]
        cifrado = cifrado + "%"

    return cifrado

def descifrar(mensaje):
    mensajeaux = ""
    descifrado= ""
    cont=0
    while cont < len(mensaje):
        if mensaje[cont] == "%":
            mensajeaux += chr(int(descifrado))
            cont+=1
            descifrado= ""
        for j in range (len(dic)):
            if dic[j] == mensaje[cont:cont+3]:
                descifrado += str(j)
        cont+=3
    return mensajeaux


mensaje= cifrar("hola")
print(mensaje)
print(descifrar(mensaje))"""

#Ejercicio 10

"""tabla = crear_tabla(136)
mensaje = 0
resultado = 0
def codificar(cadena):
    resultadofinal = ''
    for i in range (len(cadena)):
        caracter = ord(cadena[i])
        caracteraux = caracter *37
        if caracter <= 78:
            complemento = caracter + 79 - 32
        elif caracter > 78:
            complemento = caracter + 32 - 79
        caracteraux = str(caracteraux)
        resultado = ''
        for i in range(4):
            resultado += chr(int(caracteraux[i])*int(caracteraux[i]) + complemento)
        
        resultado += chr(complemento)
        resultadofinal += resultado
    return resultadofinal
    
def decodificar(mensaje):
    auxfinalstr = ""
    for i in range(0,len(mensaje),5):
        complemento = ord(mensaje[i+4])
        aux = ""
        for j in range(0,4):
            caracter = int(sqrt(ord(mensaje[i+j]) - complemento))
            aux += str(caracter)
        auxfinal = int(aux)/37
        auxfinalstr += chr(int(auxfinal))
    return auxfinalstr

mensaje = input("Ingrese un mensaje para codificar: ")
print(codificar(mensaje))

mensajecodif = input("Ingrese mensaje codificado: ")
print(decodificar(mensajecodif))
"""
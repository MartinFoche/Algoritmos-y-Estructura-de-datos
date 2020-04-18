#Ejercicio1

def fibonacci(numero):
    if(numero==0 or numero==1):
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

#Ejercicio2

def sumatoria(numero):
    if (numero == 1 or numero == 0):
        return numero
    else:
        return sumatoria(numero-1)+numero

#Ejercicio3

def multiplicacion (n,n2):
    if (n2 == 1):
        return n
    else:
        return n + multiplicacion(n,n2-1)

#Ejercicio4

def exponente(n,n2):
    if (n2==0):
        return 1

    else:
        return n * exponente(n,n2-1)

#Ejercicio5

def caracteres(sec):
    if len(sec)==1:
        return sec
    else:
        return sec[-1]+caracteres(sec[:-1])

#Ejercicio6

def fraccion(n,aux):
    if n ==1:
        return aux
    else:
        aux+=1/n
        return fraccion(n-1,aux)

#Ejercicio 7
def binario(n):
    if n==0:
        return " "
    else:
       return binario(n//2)+str(n % 2)

#Ejercicio 8
def logaritmo(base, numero):
    if(base == numero):
        return 1
    else:
        return 1 + logaritmo(base, numero/base)

#Ejercicio 9

def digitos(n):
    if n>9:
        n=n/10
        return 1+digitos(n)
    elif n<=9:
        return 1
#Ejercicio 10

def alreves(n):
    if n<=9:
        return n

#Ejercicio 11
def mcd(n1,n2):
    if n2==0:
        return n1
    else:
        return mcd(n2, n1 % n2)

#Ejercicio 12
def mcm(n,m):
    if(n % m == 0):
        return n
    else:
        return mcm(n, m * n)

#Ejercicio 13
def suma_digitos(n):
    if n<10:
        return n
    else:
        return (n%10) + suma_digitos(n//10) 

#Ejercicio14

def raiz(n,x):
    #x inicializado en 1
    if x*x == n:
        return x
    elif x*x > n:
        return x-1
    else:
        return raiz(n,x+1)

#Ejercicio 16

def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

#Ejercicio 17
def barrido_matriz(m, i, j):
    if (i<len(m) and j<len(m[i])):
        print(m[i][j])
        if(j==len(m[i][j])):
            j+=1
            j=-1
        barrido_matriz(m,i,j+1)

#Ejercicio 18
def sucesion(n):
    if n==1:
        return 2
    elif n>=2:
        return n+1/sucesion(n-1)

#Ejercicio 19
i=0
def busq_secuencial(buscado, v):
    global i
    if buscado==v[i]:
        return "El elemento se encuentra en la posicion ",i," de la lista"
    else:
        i+=1
        return busq_secuencial(buscado,v)

#Ejercicio 20
def bbin(buscado,v,pri,ult):
    if pri>ult:
        return "El elemento no se encuentra"
    med=(pri+ult)//2
    if buscado==v[med]:
        return med
    elif buscado>v[med]:
        return bbin(buscado,v,med+1,ult)
    else:
        return bbin(buscado,v,pri,med-1)


#Ejercicio 21
def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

#Ejercicio 25
def sucesion2(n):
    if n==1:
        return 3
    elif n>=2:
        return sucesion(n-1)+2*n
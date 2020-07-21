class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None


class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or lista.inicio.info>nodo.info):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and act.info<nodo.info):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    


def eliminar(lista, clave):
    dato = None
    if(lista.inicio.info == clave):
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



def busqueda(lista, clave):
    aux = lista.inicio
    while(aux is not None and aux.info != clave):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig
    

def tamanio(lista):
    return lista.tamanio


def lista_vacia(lista):
    return lista.inicio is None
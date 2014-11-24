__author__ = 'claudio'

def conjuntoDasPartes(lista):
    if len(lista) >= 1:
        geraConjunto(lista)

def geraConjunto(lista):
    rules = list()
    tam = (1 << (len(lista))) - 1
    print tam
    for i in range(1,tam):
        conj = []
        bin = intToListBin(i,len(lista))
        #print bin
        for j in range(0,len(bin)):
            if bin[j] == 1:
                conj.append(lista[j])


        complemento = geraComplemento(lista,conj)
        #print conj," ",complemento

        aux = list()
        aux.append(conj)
        aux.append(complemento)
        rules.append(aux)

    for rule in rules:
        print rule[0]," --> ",rule[1]


def geraComplemento(lista,listaElem):
    temp = list()

    for elem in lista:
        esta = False
        for j in listaElem:
            if elem == j:
                esta = True

        if not esta:
            temp.append(elem)

    return temp

def hasElem(lista,Elem):
    for i in lista:
        if i == Elem:
            return True
    return False

def intToListBin(inteiro,tamBit):
    aux = list()
    temp = inteiro
    for i in range(0,tamBit):
        if (temp & 1) == 1:
            aux.append(1)
        else :
            aux.append(0)
        temp = temp >> 1
    aux.reverse()
    return aux


conjuntoDasPartes([1,2,3,4])

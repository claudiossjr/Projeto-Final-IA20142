from distlib._backport.shutil import make_archive

__author__ = 'claudio'

def makeJoins(lista):
    Cn = {}
    for i in range(0,len(lista)-2) :
        elem = lista[i]
        for j in range(i+1,len(lista)-1):
            elem1 = lista[j]
            aux = join(elem,elem1)
            if aux != 0:
               Cn[aux] = 0
    return Cn

def hasElemIn(elemento,lista):
    for i in range(0,len(lista)-1):
        if elemento == lista[i] :
            return True
    return False

def join(elem,elem1) :
    listTemp = list()

    for i in range(0,len(elem)-1) :
        listTemp.append(elem[i])

    achou_comum = False

    aux = list()

    for i in range(0,len(elem1)-1) :
        if not hasElemIn(elem1[i],elem):
            aux.append(elem1[i])
        else :
            achou_comum = True

    if achou_comum:
        listTemp.append(aux)
    return 0

C1 = makeJoins([[1],[1,2],[1,2,3],[5,4],[2,3,4,5]])

print(C1)
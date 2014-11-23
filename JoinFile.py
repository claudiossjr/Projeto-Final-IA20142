
__author__ = 'claudio'

def makeJoins(lista):
    Cn = list()
    print lista
    for i in range(0,len(lista)-1) :
        elem = lista[i]
        print elem
        for j in range(i+1,len(lista)):
            elem1 = lista[j]
            print elem1
            aux = join(elem,elem1)
            if aux != 0:
                if not hasInList(Cn,aux):
                    Cn.append(aux)
    return Cn

def join(elem,elem1) :
    listTemp = list()

    for i in range(0,len(elem)) :
        print elem[i]
        listTemp.append(elem[i])

    achou_comum = False

    aux = list()

    for i in range(0,len(elem1)) :
        print elem1[i]
        if not hasElemIn(elem1[i],elem):
            aux.append(elem1[i])
            print aux
        else :
            achou_comum = True
            print "Entrou aqui"

    if achou_comum:
        print "Entrou aqui"
        for item in aux:
            listTemp.append(item)
        print listTemp
        return listTemp
    return 0

def hasElemIn(elemento,lista):
    for i in range(0,len(lista)):
        if elemento == lista[i] :
            return True
    return False

def hasInList(Cn,aux) :
    for item in Cn:
        if same(item,aux):
            return True
    return False

def same(item,aux):
    for i in range(0,len(item)):
        if item[i] != aux[i] :
            return False
    return True

C1 = makeJoins([[1,2],[1,3],[5,4],[2,3]])

print(C1)
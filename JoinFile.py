
__author__ = 'claudio'

def makeJoins(lista):
    Cn = list()
    #print lista
    for i in range(0,len(lista)-1) :
        elem = lista[i]
        #print elem
        for j in range(i+1,len(lista)):
            elem1 = lista[j]
            #print elem1
            aux = join(elem,elem1)
            if aux != 0:
                if not hasInList(Cn,aux):
                    Cn.append(aux)
    return Cn

def join(elem,elem1) :
    listTemp = list()
    if len(elem) != 1:
        tam = len(elem) - 1
        #print "Tamanho %d", len(elem)
        for i in range(0,len(elem)) :
            #print elem[i]
            listTemp.append(elem[i])

        achou_comum = False

        aux = list()
        countEqual = 0
        for i in range(0,len(elem1)) :
            #print elem1[i]
            if not hasElemIn(elem1[i],elem):
                aux.append(elem1[i])
               # print aux
            else :
                achou_comum = True
                countEqual = countEqual + 1
                #print "Entrou aqui"

        if achou_comum and countEqual >= tam:
            #print "Entrou aqui"
            for item in aux:
                listTemp.append(item)
                listTemp.sort()
            #print listTemp
            return listTemp
    else :
        for item in elem:
            listTemp.append(item)
        for item in elem1:
            listTemp.append(item)
        listTemp.sort()
        if elem != elem1:
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

def printList(lista):
    for element in lista:
        print "\t",element

C1 = makeJoins([["Agua"],
                ["Pao"],
                ["Cerveja"],
                ["Cebola"],
                ["Maca"]])

C2 = makeJoins(C1)

C3 = makeJoins(C2)

C4 = makeJoins(C3)

print "With 2"
print ""
printList(C1)
print ""

print "With 3"
print ""
printList(C2)
print ""

print "With 4"
print ""
printList(C3)
print ""

print "With 5"
print ""
printList(C4)
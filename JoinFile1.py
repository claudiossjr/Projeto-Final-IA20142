
__author__ = 'claudio'

class Util:

    def __init__(self):
        '''Inicializa a classe'''
        print "make join"

    def makeJoins(self,lista):
        Cn = list()
        #print lista
        for i in range(0,len(lista)-1):
            elem = lista[i]
            #print elem
            for j in range(i+1,len(lista)):
                elem1 = lista[j]
                #print elem1
                aux = self.join(elem,elem1)
                if aux != 0:
                    if not self.hasInList(Cn,aux):
                        Cn.append(aux)
        return Cn

    def join(self,elem,elem1) :
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
                if not self.hasElemIn(elem1[i],elem):
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

    def hasElemIn(self,elemento,lista):
        for i in range(0,len(lista)):
            if elemento == lista[i] :
                return True
        return False

    def hasInList(self,Cn,aux) :
        for item in Cn:
            if self.same(item,aux):
                return True
        return False

    def same(self,item,aux):
        for i in range(0,len(item)):
            if item[i] != aux[i]:
                return False
        return True

    def printList(self,lista):
        for element in lista:
            print "\t",element

class HelpTools:

    def __init__(self):
        '''Init hepTool'''
        self.rules = list()

    def conjuntoDasPartes(self,lista):
        if len(lista) > 1:
           return self.geraConjunto(lista)
        return lista

    def geraConjunto(self,lista):
        rules = list()
        tam = (1 << (len(lista))) - 1
        #print tam
        for i in range(1,tam):
            conj = []
            bin = self.intToListBin(i,len(lista))
            #print bin
            for j in range(0,len(bin)):
                if bin[j] == 1:
                    conj.append(lista[j])


            complemento = self.geraComplemento(lista,conj)
            #print conj," ",complemento

            aux = list()
            aux.append(conj)
            aux.append(complemento)
            rules.append(aux)

        return rules


    def geraComplemento(self,lista,listaElem):
        temp = list()

        for elem in lista:
            esta = False
            for j in listaElem:
                if elem == j:
                    esta = True
                    break;

            if not esta:
                temp.append(elem)

        return temp

    def hasElem(self,lista,Elem):
        for i in lista:
            if i == Elem:
                return True
        return False

    def intToListBin(self,inteiro,tamBit):
        aux = list()
        temp = inteiro
        for i in range(0,tamBit):
            if (temp & 1) == 1:
                aux.append(1)
            else :
                aux.append(0)
            temp = temp >> 1
        #aux.reverse()
        return aux

    def unionSet(self,listA,listB):
        '''Make Union between two lists'''
        listTemp = list()
        for elem in listA:
            listTemp.append(elem)
        for elem in listB:
            listTemp.append(elem)
        listTemp.sort()
        return listTemp

'''
help = HelpTools()
for rule in help.conjuntoDasPartes([1,2,3]):
    print rule[0], " --> ",rule[1]
    print help.unionSet(rule[0],rule[1])
'''

'''
help = HelpTools()
for rule in help.conjuntoDasPartes([1,2,3,4,5,6]):
    print rule[0], " --> ",rule[1]
'''

'''
util = Util()

C1 = util.makeJoins([["Agua"],  
                ["Pao"],
                ["Cerveja"],
                ["Cebola"],
                ["Maca"]])

C2 = util.makeJoins(C1)

C3 = util.makeJoins(C2)

C4 = util.makeJoins(C3)

print "With 2"
print ""
util.printList(C1)
print ""

print "With 3"
print ""
util.printList(C2)
print ""

print "With 4"
print ""
util.printList(C3)
print ""

print "With 5"
print ""
util.printList(C4)
'''

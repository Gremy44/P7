liste=[ ('a',10),('b',20),('c',10),('d',40)]
i=0

def combinaison( liste, selectionner=[]):
    #print("select>",liste,selectionner)
    if len(liste)>0:
        val1=liste.pop(0) #a              
        rest1= combinaison(liste.copy() , selectionner+[val1])

        if len(liste)==0 and  len(selectionner)==0:#pas la peine de calculer car retourn 0 et []
            return rest1
        #sinon on continue avec les autres possibillite
        rest2 =combinaison(liste.copy() ,selectionner)
        #moindre cout < 500 et rentabilite
        print('rest1',rest1)
        print('rest2',rest2)
        if rest1[0]== rest2[0]:
            return  rest1, rest2
        if rest1[0]< rest2[0]:#critere celui qui coute moin chere
            return rest1
        else:
            return rest2
    else :
            cost=0
            for p in selectionner:
                cost=cost+p[1]
            return cost,selectionner

print (combinaison(liste))
 


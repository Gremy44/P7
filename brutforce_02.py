import csv
from re import I

class BruteForce:
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def put_in_lst(self):
        '''
        - extract value from csv and push it in dict
        - take 'filePathToCSV'
        - return [('action_name1',price, profit),('action_name2','value1', 'value2'),...]
        '''
        values_container = []

        # read csv
        with open(self.pathfile, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                # create dict with {name:(price,profit)}
                values_container.append((row[0],float(row[1]), float(row[1])*float(row[2])/100))

        return values_container

    def brut_force_raw(self, wallet, elements, action_selection=[]):
        if elements:
            val1 = elements[1:]
            rest1 = self.brut_force_raw(wallet, elements.copy() , action_selection+[val1])
            
            if not elements and not action_selection:#pas la peine de calculer car retourn 0 et []
                return rest1

            rest2 = self.brut_force_raw(wallet, elements.copy(), action_selection)

            if rest1[0]== rest2[0]:
                return  rest1, rest2
            if rest1[0]< rest2[0]:#critere celui qui coute moin chere
                return rest1
            else:
                return rest2
        else :
            cost=0
            for p in action_selection:
                cost=cost+p[1]
            return cost,action_selection
        
"""def recursion_multiplication(n1, n2, i = 0):
    if i < n2:
        recursion_multiplication(n1, n2, i=i+1) + n1
    return n1

n1 = 3
n2 = 5
resultat = recursion_multiplication(n1, n2)
print(resultat)"""

path = './data/1-brut_force/data_brut_force.csv'

mes_valeur = BruteForce(path)

print(mes_valeur.brut_force_raw(500, mes_valeur.put_in_lst()))
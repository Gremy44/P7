from ast import Or
import csv

class Optimized:
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def put_in_dict(self):
        '''
        - extract value from csv and push it in dict
        - take 'filePathToCSV'
        - return {'key1':['value1', 'value2'],'key2':['value1', 'value2'],...}
        '''
        values_container = []

        with open(self.pathfile, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            # parsing
            for row in reader:
                # exclude first line
                try:
                    # excluse wrong values
                    if float(row[1]) > 0.0:
                        if float(row[2]) > 0.0:
                        # create clean list of values
                            values_container.append((row[0], int(float(row[1])*100), int(round(float(row[1])*float(row[2])/100, 2)*100)))
                except ValueError:
                    pass
        
        return values_container

    def floatToInt(self, float):
        return int(float*100)
                
    def brut_force(self, wallet, elements, action_selection = []):
        if elements:
            val1, list_val1 = self.brut_force(wallet, elements[1:], action_selection)
            val = elements[0]
            if val[1] <= wallet:
                val2, list_val2 = self.brut_force(wallet - val[1], elements[1:], action_selection + [val])
                if val1 < val2:
                    return val2, list_val2
            
            return val1, list_val1
        else:
            return sum([i[2] for i in action_selection]), action_selection

    def optimized(self, wallet, elements):
        wallet = self.floatToInt(wallet)

        matrice = [[0 for x in range(wallet + 1)] for x in range(len(elements) + 1)]

        for i in range(1, len(elements) + 1):
            for w in range(1, wallet + 1):
                if elements[i-1][1] <= w:
                    matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
                else:
                    matrice[i][w] = matrice[i-1][w]
        
        # retourne les elements en fonction de la somme

        w = wallet
        n = len(elements)
        action_selection = []

        while w >= 0 and n >= 0:
            e = elements[n-1]
            if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
                action_selection.append(e)
                w -= e[1]

            n -= 1

        ttcost = 0
        for i in action_selection:
            ttcost += i[1]/100
        
        return print("Profit : ", (matrice[-1][-1])/100), print("Total cost : ", ttcost), print("Actions selection : ", action_selection)

path = './data/2-Optimise/dataset1_Python+P7.csv'

mes_valeur = Optimized(path)

mes_valeur.optimized(500, mes_valeur.put_in_dict())
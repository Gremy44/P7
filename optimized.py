import csv
import time
import sys

class Optimized:
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def put_in_lst(self):
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

    def optimized(self, wallet, elements):

        # convert float value to int
        wallet = wallet*100
        
        # make array 
        matrice = [[0 for x in range(wallet + 1)] for x in range(len(elements) + 1)]

        # browse elements
        for i in range(1, len(elements) + 1):
            for w in range(1, wallet + 1):

                # keep the max value if lower of wallet
                if elements[i-1][1] <= w:
                    matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
                else:
                    # keep result of previous line if highter
                    matrice[i][w] = matrice[i-1][w]
        
        # return element by sum of them
        # we browse reverse the matrice for find the keeped elements 

        w = wallet
        n = len(elements)
        action_selection = []

        # while there is money in wallet and elements
        while w >= 0 and n >= 0:

            # take the last element in list
            e = elements[n-1]
            # calc the difference between two last line for find selected elements
            if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
                action_selection.append(e)
                w -= e[1]

            n -= 1

        ttcost = 0
        action_format = []
        
        for i in action_selection:
            # generate cost value
            ttcost += i[1]

            # format action selection value
            action_format.append((i[0], i[1]/100, i[2]/100))
        
        # Format total cost value
        ttcost = ttcost/100
        
        #return print("Profit : ", (matrice[-1][-1])/100), print("Total cost : ", ttcost), print("Actions selection : ", action_format)
        return [ttcost, (matrice[-1][-1])/100, action_format, wallet/100]

start_time = time.time()

#path = './data/2-Optimise/dataset2_Python+P7.csv'
path = sys.argv[1]
mes_valeur = Optimized(path)
retour_valeur = mes_valeur.optimized(500, mes_valeur.put_in_lst()) 

# retours console
print("-------------------------------------------------------------")
print("--|")
print("--| Coût : ", retour_valeur[0], " sur un porte feuille de", retour_valeur[3])
print("--| Bénéfices : ", retour_valeur[1])
print("--| Actions sélectionnées : ", retour_valeur[2])
print("--|")
print("--| Temps : %s seconds" % (time.time() - start_time))
print("-------------------------------------------------------------")
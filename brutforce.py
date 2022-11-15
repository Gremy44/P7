import csv
import time
import sys

class BruteForce:
    def __init__(self, pathfile):
        self.pathfile = pathfile

    def put_in_lst(self):
        '''
        - extract value from csv and push it in dict
        - take 'filePathToCSV'
        - return [('action_name1',price, profit),('action_name2','value1','value2'),...]
        '''
        values_container = []

        # read csv
        with open(self.pathfile, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                # create dict with {name:(price,profit)}
                values_container.append(
                    (row[0], float(row[1]), float(row[1])*float(row[2])/100))

        return values_container

    def brut_force(self, wallet, elements, action_selection=[]):

        if elements:

            # del first value of 'elements'list and return it in val1
            val1 = elements.pop(0)

            # rest1 and rest2 double recursion
            rest1 = self.brut_force(wallet, elements.copy(), action_selection + [val1])

            rest2 = self.brut_force(wallet, elements.copy(), action_selection)

            # avoid going to the comparison if at least one none
            if rest2 is None and rest1 is not None:
                return rest1

            if rest1 is None and rest2 is not None:
                return rest2

            if rest1 is None and rest2 is not None:
                return None

            # keep the best solution
            if rest1[1] > rest2[1]:
                return rest1
            else:
                return rest2

        else:
            # total and benefice calculation for return
            total = sum([action_selection[i][1] for i in range(len(action_selection))])
            benefices = sum([action_selection[i][2] for i in range(
                len(action_selection))])

            if total > wallet:
                return None
            else:
                return [total, benefices, action_selection, wallet]


start_time = time.time()

# path = 'data\1-Brut_force\data_brut_force_test.csv'
path = sys.argv[1]
mes_valeur = BruteForce(path)
print(mes_valeur.put_in_lst())
retour_valeur = mes_valeur.brut_force(500, mes_valeur.put_in_lst())

# retours console
print("-------------------------------------------------------------")
print("--|")
print("--| Coût : ", retour_valeur[0], " sur un porte feuille de", retour_valeur[3])
print("--| Bénéfices : ", retour_valeur[1])
print("--| Actions sélectionnées : ", retour_valeur[2])
print("--|")
print("--| Temps : %s seconds" % (time.time() - start_time))
print("-------------------------------------------------------------")

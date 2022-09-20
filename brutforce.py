import csv
import time
import tracemalloc

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

    def brut_force_raw(self, wallet, elements, action_selection = []):
        
        if elements:
            val1, list_val1 = self.brut_force_raw(wallet, elements[1:], action_selection)
            val = elements[0]
            if val[1] <= wallet:
                val2, list_val2 = self.brut_force_raw(wallet - val[1], elements[1:], action_selection + [val])
                if val1 < val2:
                    return val2, list_val2
            
            return val1, list_val1
        else:
            return sum([i[2] for i in action_selection]), action_selection

    def brut_force(self, wallet, elements):
        
        infos =  self.brut_force_raw(wallet, elements)

        ttcost = 0
        for i in infos[1]:
            ttcost += i[1]

        return print("Profits : ", infos[0]), print("Total cost : ", ttcost), print("Actions sélectionnées : ", infos[1])

start_time = time.time()
#tracemalloc.start()
path = './data/1-brut_force/data_brut_force.csv'

mes_valeur = BruteForce(path)

mes_valeur.brut_force(500, mes_valeur.put_in_lst())

print("--- %s seconds ---" % (time.time() - start_time))

#print(tracemalloc.get_traced_memory())
 
# stopping the library
# tracemalloc.stop()
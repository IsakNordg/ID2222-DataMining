import time

# You are to solve the first sub-problem: to implement the A-Priori algorithm for finding frequent itemsets with support at least s in a dataset of sales transactions. Remind that support of an itemset is the number of transactions containing the itemset. To test and evaluate your implementation, write a program that uses your A-Priori algorithm implementation to discover frequent itemsets with support at least s in a given dataset of sales transactions.

class Apriori:
    def __init__(self, s_precentage = 0.03, filename = 'T10I4D100K.dat'):
        
        self.s_precentage = s_precentage    # support  0.003 takes 180 seconds
        self.filename = filename            # filename
        self.frequent = {}                  # frequent itemsets

        self.data = self.readData(filename)
        self.l = len(self.data)
        self.s = self.l * self.s_precentage # Support required to be considered frequent

        self.runPasses()


    def readData(self, filename):
        # Read the data from the file
        data = [i.strip().split() for i in open(filename).readlines()]
        longest = 0

        # Find the longest transaction
        for line in data:
            if len(line) > longest:
                longest = len(line)
        self.longest = longest
        return data
    
    def runPasses(self):
        for pass_number in range(1, self.longest + 1): #self.longest):
            all = {}

            if pass_number == 3 or pass_number == 4:
                i = 0
            
            # The first pass is a special case
            if pass_number == 1:
                all = self.firstPass()
            
            else:
                for transaction in self.data:                       # For each transaction

                    alreadyVisited = []
                    for previous in self.frequent[pass_number-1]:   # For each itemset in the previous frequent itemsets
                        if type(previous) == str:
                            previous = [previous]
                        flag = False
                        for item in previous:
                            if item not in transaction:             # If at least one item in the previous itemset is not in the transaction
                                flag = True                             
                                break                               # Break out of the loop to go to the next previous itemset        
                        if flag:
                            continue
                        for item in transaction:                                # For each item in the transaction we check if it is in the previous itemset
                            itemSet = tuple(sorted(list(previous) + [item]))    # and if it is frequent. If it is, we have an itemset where all subsets are frequent, so we add it to the dictionary
                            if item not in previous and item in self.frequent[1].keys() and itemSet not in alreadyVisited:
                                alreadyVisited.append(itemSet)
                                if itemSet in all:                          # And store it in the dictionary
                                    all[itemSet] += 1
                                else:
                                    all[itemSet] = 1

            self.frequent[pass_number] = {}
            for item in all:
                if all[item] >= self.s:
                    self.frequent[pass_number][item] = all[item]


    def firstPass(self):
        all = {}
        for transaction in self.data:
            for item in transaction:
                if item in all:
                    all[item] += 1
                else:
                    all[item] = 1
        return all


    def printFrequent(self):
        for i in self.frequent:
            if len(self.frequent[i]) == 0:
                break
            
            if i == 1:
                print(f"Itemsets of size {i}:")
                for itemset in self.frequent[i]:
                    print(f"{itemset} ({self.frequent[i][itemset]}), ", end="")
                print()
                print("-----------------------")
                continue

            print(f"Itemsets of size {i}:")
            for itemset in self.frequent[i]:
                    print(f"{itemset} ({self.frequent[i][itemset]})")
            print("-----------------------")

a = Apriori()
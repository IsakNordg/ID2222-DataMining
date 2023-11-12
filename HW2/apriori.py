import time

# You are to solve the first sub-problem: to implement the A-Priori algorithm for finding frequent itemsets with support at least s in a dataset of sales transactions. Remind that support of an itemset is the number of transactions containing the itemset. To test and evaluate your implementation, write a program that uses your A-Priori algorithm implementation to discover frequent itemsets with support at least s in a given dataset of sales transactions.

class Apriori:
    def __init__(self) -> None:
        self.s_precentage = 0.03    # support
        self.c = 0.5                # confidence
        self.frequent = {}          # frequent itemsets

        self.data = self.readData('T10I4D100K.dat')
        self.l = len(self.data)
        self.s = self.l * self.s_precentage # Support required to be considered frequent
        
        self.runPasses()

        i = 0

    def readData(self, filename):
        data = [i.strip().split() for i in open("T10I4D100K.dat").readlines()]
        longest = 0

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
                        for item in transaction:                            # For each item in the transaction we check if it is in the previous itemset
                                                                            # and if it is frequent. If it is, we have an itemset where all subsets are frequent, so we add it to the dictionary
                            if item not in previous and item in self.frequent[1].keys():                        
                                itemSet = list(previous) + [item]                 # Create a new itemset
                                itemSet.sort()
                                itemSet = tuple(itemSet)
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


    def secondPass(self):
        all = {}
        for transaction in self.data:
            for i in range(len(transaction)):
                for j in range(i+1, len(transaction)):
                    if transaction[i] in self.frequent[1] and transaction[j] in self.frequent[1]:
                        itemSet = tuple((transaction[i], transaction[j]))
                        if itemSet in all:
                            all[itemSet] += 1
                        else:
                            all[itemSet] = 1
                
        self.frequent[2] = {}
        for item in all:
            if all[item] >= self.s:
                self.frequent[2][item] = all[item]
    
    def thirdPass(self):
        all = {}
        for transaction in self.data:
            for i in range(len(transaction)):
                for j in range(i+1, len(transaction)):
                    for k in range(j+1, len(transaction)):
                        if transaction[i] in self.frequent[1] and transaction[j] in self.frequent[1] and transaction[k] in self.frequent[1]:
                            itemSet = tuple((transaction[i], transaction[j], transaction[k]))
                            if itemSet in all:
                                all[itemSet] += 1
                            else:
                                all[itemSet] = 1
                
        self.frequent[3] = {}
        for item in all:
            if all[item] >= self.s:
                self.frequent[3][item] = all[item]

a = Apriori()
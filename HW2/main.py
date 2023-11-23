from apriori import * 
from ruleGeneration import *
import time

class Main:
    def __init__(self):
        # Hyperparameters
        s_precentage = 0.01
        c = 0.5

        start = time.time()
        apriori = Apriori(s_precentage=s_precentage, filename='T10I4D100K.dat')
        aprioriTime = time.time() - start
        
        apriori.printFrequent()

        start = time.time()

        ruleGeneration = RuleGeneration(frequent=apriori.frequent, c=c)
        # ruleGeneration.findRules()
        ruleGeneration.printRules()

        ruleGenerationTime = time.time() - start


        # ruleGeneration.printRules()

        print(f"Apriori took {round(aprioriTime, 2)} seconds")
        print(f"Rule generation took {round(ruleGenerationTime, 2)} seconds")
        print(f"Total time: {round(aprioriTime + ruleGenerationTime, 2)} seconds")

main = Main()
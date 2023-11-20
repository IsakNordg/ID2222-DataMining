from apriori import *
import itertools

class RuleGeneration:
    def __init__(self, frequent, c):
        self.frequent = frequent
        self.c = c
        self.rules = self.findRules()

    def findRules(self):
        rules = []
        for itemSetLength in self.frequent:
            if itemSetLength == 1:
                continue
            for itemSet in self.frequent[itemSetLength]:
                itemSet = list(itemSet)
                subsets = self.findsubsets(itemSet, len(itemSet)-1)

                for subset in subsets:
                    if len(subset) == 1:
                        leftSide = subset[0]
                    else:
                        leftSide = list(subset)
                    rightSide = list(set(itemSet) - set(subset))

                    if type(leftSide) == str:
                        conf = self.frequent[itemSetLength][tuple(itemSet)] / self.frequent[1][leftSide]
                    else:
                        conf = self.frequent[itemSetLength][tuple(itemSet)] / self.frequent[len(leftSide)][tuple(leftSide)]

                    if conf >= self.c:
                        if type(leftSide) == str:
                            leftSide = [leftSide]
                        rules.append((leftSide, rightSide, conf))

        return rules
    
    # https://www.geeksforgeeks.org/python-program-to-get-all-subsets-of-given-size-of-a-set/
    def findsubsets(self, s, n):
        subsets = []
        for i in range(1, len(s)):
            for subset in itertools.combinations(s, i):
                subsets.append(subset)
        return subsets
            
    def printRules(self):
        for rule in self.rules:
            print(f"{rule[0]} -> {rule[1]} (confidence {round(rule[2], 2)})")
        print(f"{len(self.rules)} rules found")
        print()
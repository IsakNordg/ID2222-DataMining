from shingling import *
from minhash import *
import sys, os

class Main():
    def __init__(self):
        self.readAllDocs()
        
        self.k = 10
        self.createShingles()
        
        self.minHash = MinHash(self.shingles, self.docs)

        print(self.minHash.characteristic_matrix)


    def readAllDocs(self):
        self.docs = []
        for filename in os.listdir("Data"):
            with open("Data/" + filename, "r", encoding="utf8") as f:
                doc=f.read().replace('\n', ' ')
            self.docs.append(doc)
    

    def createShingles(self):
        self.shingles = {}
        for doc in self.docs:
            self.shingles[doc] = Singling(self.k, doc)


main = Main()
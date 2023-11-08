from shingling import *
from minhash import *
from doc import *
import sys, os

class Main():
    def __init__(self):
        self.docs = self.readAllDocs()
        
        self.k = 10
        self.shingles = self.createShingles()

        self.minHash = MinHash(self.docs)
        print(self.minHash.get_similarity(self.docs[0], self.docs[1]))
        print(self.minHash.get_similarity(self.docs[2], self.docs[3]))

    def readAllDocs(self):
        docs = []
        dir = "Data"
        for filename in os.listdir(dir):
            docs.append(doc(dir + "/" + filename))
        return docs
    

    def createShingles(self):
        shingles = {}
        for doc in self.docs:
            shingles[doc.name] = doc.shingles
        return shingles


main = Main()
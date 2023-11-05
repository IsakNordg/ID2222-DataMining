import numpy as np

class MinHash():
    def __init__(self, shingles, docs):
        self.shingles = shingles
        self.docs = docs
        
        self.allShingles = self.listAllShingles()

        self.characteristicMatrix = self.createCharacteristicMatrix()
        self.nrHashFunctions = 100


    def createCharacteristicMatrix(self):
        # Tror vi måste ha antalet dokument och antalet shingles som input
        characteristicMatrix = {}
            
        for doc in self.docs:
            characteristicMatrix[doc] = {}
            for shingle in self.allShingles:
                if shingle in self.shingles[doc].shinglesHash:
                    characteristicMatrix[doc][shingle] = 1
        return characteristicMatrix


    def listAllShingles(self):
        allShingles = set()
        for shingles in self.shingles.values():
            for shingle in shingles.shinglesHash:
                if shingle not in allShingles:
                    AllShingles.add(shingle)

import numpy as np
from ordered_set import OrderedSet
from collections import defaultdict


class MinHash():
    def __init__(self, docs, k = 100):
        self.docs = docs
        self.k = k  # Amount of permutations when creating signature matrix
        
        self.allShingles = self.listAllShingles()
        self.createIndexes()
        self.characteristicMatrix = self.createCharacteristicMatrix()
        self.signatureMatrix = self.createSignatureMatrix()

    def createIndexes(self):
        self.shingleToIndex = {}
        for i, shingle in enumerate(self.allShingles):
            self.shingleToIndex[shingle] = i
        
        self.docToIndex = {}
        for i, doc in enumerate(self.docs):
            self.docToIndex[doc] = i


    def createCharacteristicMatrix(self):
        characteristicMatrix = np.zeros((len(self.docs), len(self.allShingles)), dtype=int)
            
        for doc in self.docs:
            for shingle in doc.shingles:
                characteristicMatrix[self.docToIndex[doc]][self.shingleToIndex[shingle]] = 1
        
        return characteristicMatrix

    def createSignatureMatrix(self):
        signatureMatrix = np.zeros((self.k, len(self.docs)), dtype=int)

        for i in range(self.k):
            shuffled_matrix = self.characteristicMatrix.copy()
            np.random.shuffle(shuffled_matrix.T)
            signatureMatrix[i] = np.argmax(shuffled_matrix, axis=1)

        return signatureMatrix

    def get_similarity(self, doc1, doc2):
        sign1 = self.signatureMatrix[:, self.docToIndex[doc1]]
        sign2 = self.signatureMatrix[:, self.docToIndex[doc2]]

        matches = 0
        for i in range(self.k):
            if sign1[i] == sign2[i]:
                matches += 1
        return matches / self.k

########## HELPER FUNCTIONS ##########
    def listAllShingles(self):
        allShingles = OrderedSet()
        for doc in self.docs:
            for shingle in doc.shingles:
                allShingles.add(shingle)
        return allShingles


    def printCharacteristicMatrix(self):
        print("shingle", end="\t")
        for doc in self.docs:
            print(doc.name, end="\t")
        print()
        for shingle in self.allShingles:
            print(shingle, end="\t")
            for doc in self.docs:
                print(self.characteristicMatrix[self.docToIndex[doc]][self.shingleToIndex[shingle]], end="\t")
            print()
from shingling import *
from minhash import *
from LSH import *
from doc import *
import sys, os, time

class Main():
    def __init__(self):
        startTime = time.time()

        # Hyperparameters
        self.k_shingle = 10     # Shingle size
        self.k_perm = 100       # Permutations
        self.t = 0.05            # Threshold
        self.b = 50             # Bands

        # This is used to change the data used. All text files in the folder will be read and compared
        # self.dir = "Data\sports+articles+for+objectivity+analysis\Raw data"   # NOTE: Finds no similar docs
        # self.dir = "Data\sms+spam+collection\Split"                           # NOTE: Finds some similar docs, but they are very short
        # self.dir = "DataPresidents"                                             # NOTE: Finds similar docs
        self.dir = "DataMovies"

        self.docs = self.readAllDocs()
        print("Docs read")

        
        self.shingles = self.createShingles()
        print("Shingles created")

        self.minHash = MinHash(self.docs, k = self.k_perm)
        print("MinHash created")

        self.lsh = LSH(self.minHash, b = self.b, t = self.t)
        print("LSH created")
        print()

        self.lsh.printSimilarDocs()
        
        print("Time: " + str(time.time() - startTime))
        
        self.printFacit()   # NOTE: Only works for smaller datasets, like the presidents dataset


    def readAllDocs(self):
        docs = []
        failed = 0

        # Get all files in the directory
        for filename in os.listdir(self.dir):
            if filename == "SMS1200.txt" or filename == "Text0200.txt": # Too many files to read, so we have a cutoff
                break
            try:
                docs.append(doc(self.dir + "/" + filename, k = self.k_shingle))
            except:
                failed += 1
        print("Failed to read " + str(failed) + " docs")
        return docs
    

    # Creates a dictionary with the shingles for each document
    def createShingles(self):
        shingles = {}
        for doc in self.docs:
            shingles[doc.name] = doc.shingles
        return shingles

    # Brute-forces the correct solutions for the dataset
    # NOTE: Only works for smaller datasets, like the presidents dataset
    def printFacit(self):
        print("-------------------- FACIT --------------------")
        self.allJacSim = self.getAllJacSim()

        i = 0
        for element in self.allJacSim:
            if self.allJacSim[element] > self.t:
                print(element, self.allJacSim[element]) 
                i += 1
        if i == 0:
            print("No similar documents found")

    # Just a helperfunction for the facit
    def getAllJacSim(self):
        cs = CompareSets()
        jacSim = {}
        for i in range(len(self.docs)):
            for j in range(i+1, len(self.docs)):
                if self.docs[i] != self.docs[j]:
                    jacSim[(self.docs[i].name, self.docs[j].name)] = cs.get_jaccard_similarity(self.docs[i].shingles, self.docs[j].shingles)
        return jacSim



main = Main() 
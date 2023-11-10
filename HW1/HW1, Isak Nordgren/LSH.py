from minhash import *
from ordered_set import OrderedSet

class LSH:
    def __init__(self, minHash, b, t):
        self.minHash = minHash
        self.b = b     # Bands
        self.t = t    # Threshold

        self.buckets = self.createTableForBuckets()
        self.bands = self.createBands()
        self.hashIntoBuckets()
        self.similarDocs = self.getSimilarDocs()


    def createTableForBuckets(self):
        buckets = []
        for i in range(self.b):
            buckets.append({})  # Create a dictionary for each band. This is where we will hash the signatures
        return buckets
    
    # Splits the signature matrix into b bands
    def createBands(self):
        return np.array_split(self.minHash.signatureMatrix, self.b, axis=0)
        
    # Hashes the signatures into the buckets        
    def hashIntoBuckets(self):
        for bandIndex, band in enumerate(self.bands):
            for j, column in enumerate(band.T):
                key = hash(tuple(column))
                if key not in self.buckets[bandIndex]:
                    self.buckets[bandIndex][key] = []   # Create a list for each key. If two signatures hash to the same key, they are similar
                self.buckets[bandIndex][key].append(j)

    # Returns a list of similar documents
    def getSimilarDocs(self):

        # Find all buckets with more than one signature
        similarHashes = []
        for bucket in self.buckets:
            for key in bucket:
                if len(bucket[key]) > 1:
                    similarHashes.append(bucket[key])
        
        # Find all similar documents
        similarDocs = OrderedSet()
        for hashList in similarHashes:
            for i in range(len(hashList)):
                for j in range(i+1, len(hashList)):
                    doc1 = self.minHash.docs[hashList[i]]
                    doc2 = self.minHash.docs[hashList[j]]
                    similarity = self.minHash.get_similarity(doc1, doc2)
                    if similarity >= self.t:
                        similarDocs.add((doc1.name, doc2.name, similarity))
                    else:
                        print("Similarity for " + doc1.name + " and " + doc2.name + " below threshold: " + str(similarity))
        
        return similarDocs

    def printSimilarDocs(self):
        if len(self.similarDocs) == 0:
            print("No similar docs found")
            return

        i = 0
        for doc1, doc2, similarity in self.similarDocs:
            print(doc1 + " and " + doc2 + " are similar with Jaccard-similarity " + str(similarity))
            i += 1
        print(str(i) + " similar docs found")
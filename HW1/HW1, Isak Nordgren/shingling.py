import sys
from ordered_set import OrderedSet

class Shingling():
    def __init__(self, k, content):
        self.k = k  # Shingle size
        self.content = content  # The content of the document
        self.shingles = self.get_shingles() # The shingles of the document
        self.shinglesHash = self.get_shingles_hash() # The shingles of the document hashed

    # Creates an ordered set of all shingles in the document
    def get_shingles(self):
        shingles = OrderedSet()
        for i in range(len(self.content) - self.k + 1):
            shingles.add(self.content[i:i + self.k])
        return shingles
    
    # Creates an ordered set of all shingles in the document hashed
    def get_shingles_hash(self):
        shinglesHash = OrderedSet()
        for shingle in self.shingles:
            shinglesHash.add(hash(shingle))
        return shinglesHash
    

class CompareSets():
    def __init__(self):
        pass

    def get_intersection(self, set1, set2):
        return set1.intersection(set2)

    def get_union(self, set1, set2):
        return set1.union(set2)
    
    def get_jaccard_similarity(self, set1, set2):
        return len(self.get_intersection(set1, set2)) / len(self.get_union(set1, set2))


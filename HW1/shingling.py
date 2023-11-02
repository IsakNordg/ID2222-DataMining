import sys

class Singling():
    def __init__(self, k, doc):
        self.k = k
        self.doc = doc
        self.shingles = self.get_shingles()
        self.shingles_hash = self.get_shingles_hash()
        self.shingles_hash_list = list(self.shingles_hash)
        self.shingles_hash_list.sort()

    def get_shingles(self):
        shingles = set()
        for i in range(len(self.doc) - self.k + 1):
            shingles.add(self.doc[i:i + self.k])
        return shingles
    
    def get_shingles_hash(self):
        shingles_hash = set()
        for shingle in self.shingles:
            shingles_hash.add(hash(shingle))
        return shingles_hash
    
class CompareSets():
    def __init__(self):
        pass

    def get_intersection(self, set1, set2):
        return set1.intersection(set2)

    def get_union(self, set1, set2):
        return set1.union(set2)
    
    def get_jaccard_similarity(self, set1, set2):
        return len(self.get_intersection(set1, set2)) / len(self.get_union(set1, set2))

    
def main():
    with open("Data/SW_3.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    SW3 = Singling(10, doc)

    with open("Data/SW_4.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    SW4 = Singling(10, doc)

    with open("Data/SW_5.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    SW5 = Singling(10, doc)

    with open("Data/SW_6.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    SW6 = Singling(10, doc)

    with open("Data/LOTR_1.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    LOTR1 = Singling(10, doc)

    with open("Data/LOTR_2.txt", "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    LOTR2 = Singling(10, doc)

    cs = CompareSets()
    print("SW:")
    print("3, 4: " + str(cs.get_jaccard_similarity(SW3.shingles_hash, SW4.shingles_hash)))
    print("3, 5: " + str(cs.get_jaccard_similarity(SW3.shingles_hash, SW5.shingles_hash)))
    print("3, 6: " + str(cs.get_jaccard_similarity(SW3.shingles_hash, SW6.shingles_hash)))
    print("4, 5: " + str(cs.get_jaccard_similarity(SW4.shingles_hash, SW5.shingles_hash)))
    print("4, 6: " + str(cs.get_jaccard_similarity(SW4.shingles_hash, SW6.shingles_hash)))
    print("5, 6: " + str(cs.get_jaccard_similarity(SW5.shingles_hash, SW6.shingles_hash)))

    print("LOTR:")
    print("LOTR1, LOTR2: " + str(cs.get_jaccard_similarity(LOTR1.shingles_hash, LOTR2.shingles_hash)))
    print("LOTR1, SW3: " + str(cs.get_jaccard_similarity(LOTR1.shingles_hash, SW3.shingles_hash)))
    print("LOTR1, SW4: " + str(cs.get_jaccard_similarity(LOTR1.shingles_hash, SW4.shingles_hash)))
    print("LOTR1, SW5: " + str(cs.get_jaccard_similarity(LOTR1.shingles_hash, SW5.shingles_hash)))
    print("LOTR1, SW6: " + str(cs.get_jaccard_similarity(LOTR1.shingles_hash, SW6.shingles_hash)))
    

if __name__ == "__main__":
    main()


"""
    

    def get_shingles_hash_list(self):
        shingles_hash_list = []
        for shingle in self.shingles:
            shingles_hash_list.append(hash(shingle))
        return shingles_hash_list

    def get_shingles_hash_list_sorted(self):
        shingles_hash_list = self.get_shingles_hash_list()
        shingles_hash_list.sort()
        return shingles_hash_list

    def get_shingles_hash_list_sorted_str(self):
        shingles_hash_list = self.get_shingles_hash_list_sorted()
        shingles_hash_list_str = []
        for shingle in shingles_hash_list:
            shingles_hash_list_str.append(str(shingle))

        return shingles_hash_list_str
"""
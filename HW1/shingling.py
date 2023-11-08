import sys
from ordered_set import OrderedSet

class Shingling():
    def __init__(self, k, content):
        self.k = k
        self.content = content
        self.shingles = self.get_shingles()
        self.shinglesHash = self.get_shingles_hash()

    def get_shingles(self):
        shingles = OrderedSet()
        for i in range(len(self.content) - self.k + 1):
            shingles.add(self.content[i:i + self.k])
        return shingles
    
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


def get_shingling_from_doc(path):
    with open(path, "r", encoding="utf8") as f:
        doc=f.read().replace('\n', ' ')
    return Shingling(10, doc)

def main():
    Bengt1 = get_shingling_from_doc("Data/Bengt1.txt")
    Bengt2 = get_shingling_from_doc("Data/Bengt2.txt")
    Bengt3 = get_shingling_from_doc("Data/Bengt3.txt")
    Bengt4 = get_shingling_from_doc("Data/Bengt4.txt")

    cs = CompareSets()
    print("Bengt:")
    print("1, 2: " + str(cs.get_jaccard_similarity(Bengt1.shinglesHash, Bengt2.shinglesHash)))
    print("3, 4: " + str(cs.get_jaccard_similarity(Bengt3.shinglesHash, Bengt4.shinglesHash)))


if __name__ == "__main__":
    main()


"""
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
"""
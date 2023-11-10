from shingling import *

class doc:
    def __init__(self, path, k):
        self.path = path 
        self.k = k
        self.name = path.split("/")[-1]
        self.shingles = self.get_shingling_from_doc().shinglesHash

    # Creates a shingling object (containing all shingles) from the document
    def get_shingling_from_doc(self):
        with open(self.path, "r", encoding="utf8") as f:
            content=f.read().replace('\n', ' ')
        return Shingling(self.k, content)
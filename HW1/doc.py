from shingling import *

class doc:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1]
        self.shingles = self.get_shingling_from_doc().shinglesHash

    def get_shingling_from_doc(self):
        with open(self.path, "r", encoding="utf8") as f:
            content=f.read().replace('\n', ' ')
        return Shingling(10, content)
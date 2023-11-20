from triestBase import TriestBase

class Main:
    def __init__(self):
        self.TriestBase = TriestBase(10000)
        self.file = self.openFile("web-Google.txt")

    def openFile(self, fileName):
        file = open(fileName, "r")
        while line := file.readline():
            if line[0] == "#":
                continue
            return file
    
    def next(self):
        nextLine = self.file.readline()
        if not nextLine:
            print("End of file")
            return True
        edge = nextLine.split()
        self.TriestBase.update((int(edge[0]), int(edge[1])))

    def run(self, iterations = None):
        if iterations:
            for i in range(iterations):
                if i % 1000 == 0:
                    print(i)
                self.next()
        else:
            endOfFile = False
            while not endOfFile:
                endOfFile = self.next()
    

main = Main()
main.run(20000)
print(main.TriestBase.tau)
from triestBase import TriestBase
from triestImpr import TriestImpr
import time

class Main:
    def __init__(self, M=10000, algorithm="Base"):
        self.M = M
        if algorithm.lower() == "base":
            self.Triest = TriestBase(M)
        elif algorithm.lower() == "impr":
            self.Triest = TriestImpr(M)
        
        # self.file = self.openFile("web-Stanford.txt")

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
        for i in range(len(edge)):
            edge[i] = int(edge[i])
        edge.sort()
        
        self.Triest.update((int(edge[0]), int(edge[1])))

    def runFromStream(self, iterations = None):
        if iterations:
            for i in range(iterations):
                if i % 1000 == 0:
                    print(i, self.Triest.tau)
                self.next()
        else:
            endOfFile = False
            while not endOfFile:
                endOfFile = self.next()
    
    def runBuffered(self):
        start = time.time()
        with open("web-Stanford-noDupes.txt", "r") as file:
            for line in file:
                # Skip comments and empty lines
                if line[0] == "#" or line[0] == "\n":
                    continue
                
                # Split line into two int nodes and sort them
                edge = line.split()
                for i in range(len(edge)):
                    edge[i] = int(edge[i])
                edge.sort()
                
                self.Triest.update((int(edge[0]), int(edge[1])))

                if self.Triest.t % 50000 == 0:
                    print(self.Triest.t, self.Triest.tau, self.Triest.getEstimate())
        self.printResults(start)

    def printResults(self, start):
        print("Model:", self.Triest.__class__.__name__)
        print("Estimated number of triangles:", self.Triest.getEstimate())
        # 11329473 is the real number of triangles in the dataset web-Stanford.txt
        print("Real number of triangles:", 11329473, "difference:", abs(self.Triest.getEstimate() - 11329473),
               "(" + str(round((self.Triest.getEstimate() - 11329473) / 11329473 * 100, 3)) + "%)")
        print("Number of datapoints:", self.Triest.t, "Tau:", self.Triest.tau)
        print("Execution time with M =", self.Triest.M, ":", time.time() - start)

def runTests(n = 5):
    estimates = []
    estimates_diff = []
    estimates_diff_precentage = []
    times = []
    for i in range(n):
        start = time.time()
        main = Main(M=50000, algorithm="Impr")
        main.runBuffered()
        estimates.append(main.Triest.getEstimate())
        estimates_diff.append(main.Triest.getEstimate() - 11329473)
        estimates_diff_precentage.append(str(round((main.Triest.getEstimate() - 11329473) / 11329473 * 100, 3)) + "%")
        times.append(time.time() - start)
        print()

        if i != n - 1:
            del main
            del start

        
    # print final results
    print("Results of running", n, "tests with M =", main.M, "and algorithm =", main.Triest.__class__.__name__)
    for i in range(len(estimates)):
        print("    -Test", i + 1, 
              "estimate:", estimates[i], 
              "difference:", estimates_diff[i], 
              "(" + estimates_diff_precentage[i] + ")",
              "time:", round(times[i]), "seconds")
    print("Average error is: ", sum(abs(estimates_diff)) / len(estimates_diff), "(" + str(round(sum(abs(estimates_diff)) / len(estimates_diff) / 11329473 * 100, 3)) + "%)")

runTests()

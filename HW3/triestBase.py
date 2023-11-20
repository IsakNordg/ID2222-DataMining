import random
from ordered_set import OrderedSet

class TriestBase:
    def __init__(self, M):
        self.M = M
        self.t = 0
        self.S = OrderedSet()
        self.tau = 0
        self.counters = dict()

    def update(self, edge):
        self.t += 1
        if self.sampleEdge(edge):
            self.S.add(edge)
            self.updateCounters(edge, 1)

    def sampleEdge(self, edge):
        if self.t <= self.M:
            return True
        elif random.random() <= self.M / self.t:
            randEdge = random.sample(self.S, 1)[0]
            self.S.remove(randEdge)
            self.updateCounters(randEdge, -1)
            return True
        return False
    
    def updateCounters(self, edge, sign):
        N_u = self.getNeighbours(edge[0])
        N_v = self.getNeighbours(edge[1])
        common = N_u.intersection(N_v)
        for node in common:
            # τ ← τ • 1
            self.tau += sign

            # τ_c ← τ_c • 1
            if node not in self.counters:
                self.counters[node] = 0
            self.counters[node] += sign

            # τ_u ← τ_u • 1
            # τ_v ← τ_v • 1
            self.incrementLocalCounters(edge, sign)

            # Remove nodes with no triangles from counters to save memory space
            if self.counters[node] <= 0:
                del self.counters[node]
    
    def getNeighbours(self, node):
        neighbours = set()
        for edge in self.S:
            if node in edge:
                neighbours.add(edge[0] if edge[0] != node else edge[1])
        return neighbours
    
    def incrementLocalCounters(self, edge, sign):
        if edge[0] not in self.counters:
            self.counters[edge[0]] = 0
        self.counters[edge[0]] += sign

        if edge[1] not in self.counters:
            self.counters[edge[1]] = 0
        self.counters[edge[1]] += sign

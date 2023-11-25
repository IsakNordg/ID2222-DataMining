import random
from ordered_set import OrderedSet

class TriestBase:
    def __init__(self, M):
        self.M = M
        self.t = 0
        self.S = set()
        self.tau = 0
        self.counters = dict()
        self.neighbors = dict()

    def update(self, edge):
        if edge in self.S:
            return

        self.t += 1
        if self.sampleEdge(edge):
            self.S.add(edge)
            self.updateCounters(edge, 1)
            self.updateNeighbors(edge, 1)

    def sampleEdge(self, edge):
        if self.t <= self.M:
            return True
        elif random.random() <= self.M / self.t:
            randEdge = random.sample(self.S, 1)[0]
            self.S.remove(randEdge)
            self.updateCounters(randEdge, -1)
            self.updateNeighbors(randEdge, -1)
            return True
        return False
    
    def updateCounters(self, edge, sign):
        N_u = self.getNeighbours(edge[0])
        N_v = self.getNeighbours(edge[1])
        common = N_u.intersection(N_v)

        for c in common:
            # τ ← τ • 1
            self.tau += sign

            # τ_u, τ_v, τ_c ← τ_u • 1, τ_v • 1, τ_c • 1
            # self.incrementLocalCounters(edge, c, sign)

    def updateNeighbors(self, edge, sign):
        if edge[0] not in self.neighbors:
            self.neighbors[edge[0]] = set()
        if edge[1] not in self.neighbors:
            self.neighbors[edge[1]] = set()

        if sign == 1:
            self.neighbors[edge[0]].add(edge[1])
            self.neighbors[edge[1]].add(edge[0])
        elif sign == -1:
            self.neighbors[edge[0]].remove(edge[1])
            self.neighbors[edge[1]].remove(edge[0])

    def getNeighbours(self, node):
        if node not in self.neighbors:
            return set()
        return self.neighbors[node]
    
    def incrementLocalCounters(self, edge, c, sign):
        # τ_u ← τ_u • 1    
        if edge[0] not in self.counters:
            self.counters[edge[0]] = 0
        self.counters[edge[0]] += sign

        # Remove nodes with no triangles from counters to save memory space
        if self.counters[edge[0]] <= 0:
            del self.counters[edge[0]]

        # τ_v ← τ_v • 1
        if edge[1] not in self.counters:
            self.counters[edge[1]] = 0
        self.counters[edge[1]] += sign

        if self.counters[edge[1]] <= 0:
            del self.counters[edge[1]]

        # τ_c ← τ_c • 1
        if c not in self.counters:
            self.counters[c] = 0
        self.counters[c] += sign

        if self.counters[c] <= 0:
            del self.counters[c]

    def getEstimate(self):
        xi = max(1, (self.t * (self.t - 1) * (self.t - 2)) / (self.M * (self.M - 1) * (self.M - 2)))
        return round(self.tau * xi)

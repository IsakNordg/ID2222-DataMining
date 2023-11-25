import random
from edge_sample import EdgeSample
from collections import defaultdict

class TriestBase:
    def __init__(self,M):
        self._M = M
        self._sample = EdgeSample()
        self._globalT = 0
        self._localT = {}
        self._t = 0

    def sample_edge(self,u,v):
        if self._t <= self._M:
            return True
        elif self.flip_biased_coin():
            u_dash, v_dash = self._sample.remove_random_edge()
            self.update_counters(u_dash,v_dash,'-')
            return True
        return False

    def update_counters(self,u,v,op):
        common_neighborhood = self._sample.get_intersection_neighborhood(u,v)
        
        if not common_neighborhood:
            return

        for c in common_neighborhood:

            if op == '+':
                self._globalT += 1

            elif op == '-':
                self._globalT -= 1
                

    def flip_biased_coin(self):
        head_prob = random.random()

        if head_prob <= self._M/self._t:
            return True
        else:
            return False

    def return_counters(self):
        estimate = max(1, (self._t * (self._t - 1) * (self._t - 2))/(self._M * (self._M - 1) * (self._M - 2)))

        global_estimate = int(estimate * self._globalT)

        for key in self._localT:
            self._localT[key] = int(self._localT[key] * estimate)

        return {'global':global_estimate,'local':self._localT, 'diff': 11329473 - global_estimate}

    def run(self,u,v):
        
        self._t += 1
        if self.sample_edge(u,v):
            self._sample.add_edge(u,v)
            self.update_counters(u,v,'+')


def held_karp(G, complete=True):
    '''
    held_karp(graph) -> optimal value

    Finds exact optimal value for the TSP instance:
        graph: adjlist representation of a complete graph
        optimal value: float

    TO DO:
    - solution reconstruction
    - multithreading

    A. Valitov 2017
    '''
    from itertools import combinations
    import threading

    def init_nodes(G):
        'Pulls random start node and a tuple of remaining nodes from adjlist representation of a graph'
        from itertools import combinations
        node_set = set()
        for start in G:
            node_set.update(list(G[start].keys())+[start])
        start = node_set.pop()
        total = node_set.union(set([start]))
        return start,node_set,total

    class Codes:
        'Encodes and decodes subset mappings (needed for hashtables)'
        def __init__(self,base_set):
            self.ordering = list(base_set)
            self.ordering_map = {self.ordering[i]:i for i in range(len(self.ordering))}

        def encode(self,subset):
            'subset -> code'
            code = ''.join('1' if element in subset else '0' for element in self.ordering)
            return code

        def decode(self,code):
            'code -> subset' # don't need it actually
            subset = set([self.ordering[i] for i in range(len(code)) if code[i] == '1'])
            return subset

        def no_element(self,code,element):
            'code -> code with element bit set to 0'
            i = self.ordering_map[element]
            return code[:i]+'0'+code[i+1:]

    class ThreadCont:
        'Contins computanionally intensive threads running within main (will add multithreading later)'
        def __init__(self,G):
            self.graph = G
            self.start, self.rest, self.total = init_nodes(G)
            self.size = len(self.total)
            self.coding = Codes(self.total)
            self.array = {1:{self.coding.encode(set([self.start])):{self.start:0}}}

        def main(self):
            for sub_size in range(2, self.size+1):
                self.array[sub_size] = {}
                subset_iter = combinations(tuple(self.rest),sub_size-1)
                self.thread(subset_iter,sub_size)
                del self.array[sub_size-1]
            return min([self.array[self.size][self.coding.encode(self.total)][j] + self.graph[j][self.start] for j in self.rest])

        def thread(self,subsets,sub_size):
            for subset in subsets:
                subset = set(subset)
                subset_w_start = subset | set([self.start])
                subset_code = self.coding.encode(subset_w_start)
                self.array[sub_size][subset_code] = {}
                for node in subset:
                    presubset = subset_w_start - set([node])
                    presubset_code = self.coding.no_element(subset_code,node)
                    self.array[sub_size][subset_code][node] = min([
                        self.array[sub_size-1].get(presubset_code,{}).get(k,float('inf')) + self.graph[k][node]
                            for k in presubset])

    inst = ThreadCont(G)
    return inst.main()

if __name__=='__main__':

    def get_data(file):
        n = int(file.readline())
        i = 1
        data = {}
        for line in file:
            data[i] = {'x':float(line.split()[0]),'y':float(line.split()[1])}
            i += 1
        return n,data

    def calc_dist(dot1,dot2):
        'Calculates euc distance between two points given coordinates'
        import numpy as np
        res = np.power((dot1['x']-dot2['x']),2)+np.power((dot1['y']-dot2['y']),2)
        res = np.sqrt(res)
        return res

    def make_graph(data):
        'Makes adjlist representation of a complete graph'
        G = {}
        nodes = set(data.keys())
        for u in nodes:
            G[u] = {}
            for v in nodes - set([u]):
                G[u][v] = calc_dist(data[u],data[v])
        return G

    import sys
    if len(sys.argv) == 1:
        file = sys.stdin
    else:
        file = open(sys.argv[1],'r')
    n,data = get_data(file)
    G = make_graph(data)
    res = held_karp(G)
    print('Optimal value: ',res)

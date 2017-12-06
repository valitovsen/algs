
def dijsktra(graph, source):
    '''
    dijsktra(graph,source) -> dict of shortest paths from the source

    Computes shortest paths from the source to every other node
    in directed graph with nonnegative edgeweights:
        graph - adjlist representation in dict form: {vertex1:{neighbour_1:distance,
                neighbour_2:distance,...},...}
        source - name of the source vertex as given in graph dict

    A. Valitov 2017
    '''
    import heapq

    class Cont:
        'Container to hold nonlocal variables'
        def __init__(self,graph,source):
            self.graph = graph
            self.source = source
            self.connected = set()
            self.dfs(source) # run DFS to identify reachable nodes

        def dfs(self,i):
            'Recursive DFS implementaion'
            self.connected.add(i)
            neighbours = self.graph.get(i).keys()
            if neighbours:
                for j in neighbours:
                    if j not in self.connected:
                        self.dfs(j)

        def dijsktra(self):
            'Calculates shortest paths'
            #1. Initialization
            self.explored = set([self.source])
            self.distances = {self.source:0}
            self.neighbours_to_scores = self.graph[self.source] # list of candidate nodes
            self.scores_to_neighbours = {score:set() for score in set(self.neighbours_to_scores.values())} # reversed mapping for quick look-ups
            for vert in self.neighbours_to_scores:
                self.scores_to_neighbours[self.neighbours_to_scores[vert]].add(vert)
            self.scores_heap = list(self.scores_to_neighbours.keys()) # heap to extract min greedy score in O(logn) time
            heapq.heapify(self.scores_heap)
            self.scores_heap_bl = {} # heap black list as a replacement for .delete method (absent in heapq)
            #2. Main loop
            while self.explored != self.connected:
                min_score = heapq.heappop(self.scores_heap) # extract smallest greedy score
                while self.scores_heap_bl.get(min_score, 0): # check that score is not 'deleted', if so pick extract one
                    self.scores_heap_bl[min_score] -= 1
                    min_score = heapq.heappop(self.scores_heap)
                w = self.scores_to_neighbours[min_score].pop() # find corresponding node
                self.distances[w] = min_score # update shortest distances
                self.explored.add(w) # mark w as explored
                self.update_scores(w)

        def update_scores(self,w):
            'Updates greedy scores after iteration'
            del self.neighbours_to_scores[w] # w is no longer a candidate since it's visited
            for vert in self.graph[w]: # check all w's neighbours
                if vert in self.neighbours_to_scores: # if neighbour is already a candidate (neighbour to other node in explored)
                    if self.graph[w][vert]+self.distances[w] < self.neighbours_to_scores[vert]: # update greedy score of the node if it's better
                        old_score = self.neighbours_to_scores[vert]
                        new_score = self.graph[w][vert]+self.distances[w]
                        if old_score in self.scores_heap_bl: # 'delete' old score from heap via black listing
                            self.scores_heap_bl[old_score] += 1
                        else:
                            self.scores_heap_bl[old_score] = 1
                        heapq.heappush(self.scores_heap,new_score) # push new score to the heap
                        self.neighbours_to_scores[vert] = new_score # update node's score
                        self.scores_to_neighbours[old_score].remove(vert) # remove node from old score mapping
                        if new_score in self.scores_to_neighbours: # add new score and node to mapping
                            self.scores_to_neighbours[new_score].add(vert)
                        else:
                            self.scores_to_neighbours[new_score] = set([vert])
                    else:
                        pass
                elif vert not in self.explored: # if neighbour is not a candidate and is not explored
                    score = self.graph[w][vert]+self.distances[w] # compute score
                    self.neighbours_to_scores[vert] = score # add node to candidates
                    heapq.heappush(self.scores_heap, score) # push score to the heap
                    if score in self.scores_to_neighbours: # update mapping
                        self.scores_to_neighbours[score].add(vert)
                    else:
                        self.scores_to_neighbours[score] = set([vert])

        def run(self):
            self.dijsktra()
            return self.distances

    inst = Cont(graph, source)
    return inst.run()

if __name__ == '__main__':
    '''
    -d graph representation
    -s source node
    '''
    import sys

    def getopts(argv):
        "Collects command-line options in a dictionary"
        opts = {}
        while argv:
            if argv[0][0] == '-':
                opts[argv[0]] = argv[1]
                argv = argv[2:]
            else:
                argv = argv[1:]
        return opts

    opts=getopts(sys.argv)
    temp = {'-d':'data','-s':'source node'}
    for key in temp:
        if key not in opts:
            print('%s not given, breaking...' %temp[key])
            break
    G = {}
    with open(opts['-d'],'r') as file:
        for line in file:
            raw = line.rstrip().split()
            G[int(raw[0])] = {int(pair.split(',')[0]):int(pair.split(',')[1]) for pair in raw[1:]}
    res = dijsktra(G,int(opts['-s']))
    print('Shortest distances:\n',res)

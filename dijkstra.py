
def dijkstra(graph, source):
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

        def dijkstra(self):
            'Calculates shortest paths'
            #1. Initialization
            self.not_explored = self.connected-set([self.source])
            self.distances = {self.source:0}
            self.nodes_to_scores = {} # nodes to scores mapping
            self.scores_to_nodes = {} # scores to set of nodes mapping
            for node in self.connected:
                score = self.graph[source].get(node, float('inf'))
                self.nodes_to_scores[node] = score
                self.scores_to_nodes[score] = self.scores_to_nodes.get(score, set()).union(set([node]))
            self.scores_heap = list(self.scores_to_nodes.keys())
            heapq.heapify(self.scores_heap) # heap to extract min greedy score in O(logn) time
            #2. Main loop
            while self.not_explored:
                min_score = heapq.heappop(self.scores_heap) # extract smallest greedy score
                while not self.scores_to_nodes[min_score]: # keep extracting until set is not empty
                    min_score = heapq.heappop(self.scores_heap)
                w = self.scores_to_nodes[min_score].pop() # pop node from set with relevant score
                self.distances[w] = min_score # update shortest distances
                self.not_explored.remove(w) # mark w as explored
                self.update_scores(w)

        def update_scores(self,w):
            'Updates greedy scores after iteration'
            for vert in self.graph[w]: # check all w's neighbours
                if vert in self.not_explored: # unexplored nodes
                    old_score = self.nodes_to_scores[vert]
                    new_score = min(self.nodes_to_scores[vert], self.distances[w]+self.graph[w].get(vert, float('inf')))
                    self.nodes_to_scores[vert] = new_score
                    self.scores_to_nodes[old_score].remove(vert)
                    if new_score in self.scores_to_nodes:
                        self.scores_to_nodes[new_score].add(vert)
                    else:
                        self.scores_to_nodes[new_score] = set([vert])
                    heapq.heappush(self.scores_heap,new_score) # push new score to heap

        def run(self):
            self.dijkstra()
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
    res = dijkstra(G,int(opts['-s']))
    print('Shortest distances:\n',res)

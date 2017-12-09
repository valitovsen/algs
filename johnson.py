
def johnson(G):
    '''
    johnson(graph) -> dict of shortest paths between all pairs of nodes,
                                False if negative cycle is detected

    Computes shortest paths between all pairs of nodes
    in directed weighted graph (negative edge weights are ok):
        graph - adjlist representation in dict form: {vertex1:{neighbour_1:distance,
                neighbour_2:distance,...},...}
        dict of shortest path - dict in form {source:{node: shortest distance,..},..},
                where source is every node in graph

    A. Valitov 2017
    '''
    from bellman import bellman
    from dijkstra import dijkstra

    def make_node_list(G):
        'Pulls set of all nodes from adjlist representation of a graph'
        node_list = set()
        for start in G:
            node_list.update(list(G[start].keys())+[start])
        return node_list

    def modify_weights(G,temp_dists):
        'Makes edge weights in graph non-negative using distances from temp-source run of Bellman-Ford'
        del G['temp']
        for start in G:
            for end in G[start]:
                G[start][end] = G[start][end] + temp_dists[start] - temp_dists[end]
        return G

    node_list = make_node_list(G)
    G['temp'] = {node:0 for node in node_list} # temp source to calculate distances and check for negative cycles
    temp_dists = bellman(G,'temp') # temp source distances
    if temp_dists: # no negative cost cycle
        G_modified = modify_weights(G,temp_dists) # modified graph with non-negative edge weights
        APSP = {} # All-pairs shortest paths, answer
        for source in node_list: # iter through every node
            paths = dijkstra(G_modified, source)
            for end in paths: # recompute original distances
                paths[end] = paths[end] - temp_dists[source] + temp_dists[end]
            APSP[source] = paths
        return APSP
    else: # negative cycle detected
        return None



if __name__=='__main__':
    import sys
    if len(sys.argv) == 1:
        file = sys.stdin
    else:
        file = open(sys.argv[1])
    G = {}
    for line in file:
        raw = line.rstrip().split()
        G[int(raw[0])] = {int(pair.split(',')[0]):int(pair.split(',')[1]) for pair in raw[1:]}
    res = johnson(G)
    print(res)


def bellman(graph, source):
    '''
    bellman(graph,source) -> dict of shortest paths from the source,
                                False if negative cycle is detected

    Computes shortest paths from the source to every other node
    in directed weighted graph (negative edge weights are ok):
        graph - adjlist representation in dict form: {vertex1:{neighbour_1:distance,
                neighbour_2:distance,...},...}
        source - name of the source vertex as given in graph dict

    A. Valitov 2017
    '''

    def make_lists(graph):
        'Make list of nodes and adj list with reversed edges'
        node_list = set()
        reversed_edge_list = {}
        for start in graph:
            node_list.add(start)
            for end in graph[start]:
                node_list.add(end)
                if end not in reversed_edge_list:
                    reversed_edge_list[end] = {}
                reversed_edge_list[end][start] = graph[start][end]
        return node_list, reversed_edge_list
    #1. Initialization
    node_list, reversed_edge_list = make_lists(graph)
    dyn_array = {0:{node:float('inf') for node in node_list}} #base cases
    dyn_array[0][source] = 0
    n = len(node_list)
    #2. Main loop
    for i in range(1,n): # node limit in path
        comp = True # needed for early halt or negative cost cycle detection
        dyn_array[i] = {}
        for end in node_list:
            opt1 = dyn_array[i-1][end] # shortest path under previous node limit
            opt2 = min([dyn_array[i-1][start]+graph[start][end] # shortest path under current node limit
                            for start in reversed_edge_list.get(end,[])])
            dyn_array[i][end] = min(opt1,opt2) # pick minimum
            comp = comp & (dyn_array[i-1][end] == dyn_array[i][end]) # check progress, False if paths were changed
        del dyn_array[i-1] # memory optimization, won't need it in further steps

    return {True:dyn_array[n-1],False:False}[comp] # comp after n-th iteration is False => paths were changed =>
                                                   # negative cycle is present => calculated paths may be incorrect

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
    res = bellman(G,int(opts['-s']))
    if res:
        print('Shortest distances:\n',res)
    else:
        print('Detected negative cycle')

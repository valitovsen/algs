<h2>Python Implementation of Classic Algorithms</h2>

<h3>Contents</h3>
<p>Dynamic Programming:</p>
<ul>
  <li><b>Knapsack problem</b> - recursive implementation of DP algorithm to solve 0-1 knapsack problem [<a href="knapsack.py">code</a>][<a href="https://en.wikipedia.org/wiki/Knapsack_problem">wiki</a>]</li>
  <li><b>Held-Karp Algorithm</b> - exact DP algorithm to solve the Travelling Salesman Problem in <i>O(n<sup>2</sup>2<sup>n</sup>)</i> time [<a href="tsp.py">code</a>][<a href="https://en.wikipedia.org/wiki/Travelling_salesman_problem">wiki</a>]</li>
  <li><b>Needleman-Wunsch Algorithm</b> - implementation of Needleman-Wunsch algorithm to find optimal alignment of two sequences [<a href="knapsack.py">code</a>][<a href="https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm">wiki</a>][<a href="http://www.sciencedirect.com/science/article/pii/0022283670900574?via%3Dihub">paper</a>]</li>
  <li><b>Bellman-Ford Algorithm</b> - DP algorithm to find the shortest paths from the source to every other node in a directed weighted graph with no negative-weight cycle in <i>O(|E||V|)</i> time  [<a href="bellman.py">code</a>][<a href="https://en.wikipedia.org/wiki/Bellman–Ford_algorithm">wiki</a>]</li>
  <li><b>Johnson's Algorithm</b> - algorithm to find the shortest paths between all pairs of nodes in a directed weighted graph with no negative-weight cycle in <i>O(|V||E|log|V|)</i> time (based on single run of Bellman-Ford algorithm and V runs of Dijkstra's algorithm) [<a href="johnson.py">code</a>][<a href="https://en.wikipedia.org/wiki/Johnson%27s_algorithm">wiki</a>]</li>
 </ul>
<p>Greedy Algorithms:</p>
<ul>
  <li><b>Clustering</b> - max-spacing k-clustering algorithm [<a href="knapsack.py">code</a>][<a href="https://en.wikipedia.org/wiki/Knapsack_problem">wiki</a>]</li>
  <li><b>Huffman's Algorithm</b> - algorithm to obtain optimal coding scheme given frequences of characters [<a href="huffman.py">code</a>][<a href="https://en.wikipedia.org/wiki/Huffman_coding">wiki</a>][<a href="http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf">paper</a>]</li>
  <li><b>Dijkstra's Algorithm</b> - heap-based greedy algorithm to find the shortest paths from the source to every other node in a directed graph with non-negative edge weights in <i>O(|E|log|V|)</i> time  [<a href="dijkstra.py">code</a>][<a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">wiki</a>][<a href="http://www-m3.ma.tum.de/foswiki/pub/MN0506/WebHome/dijkstra.pdf">paper</a>]</li>
  <li><b>Prim's Algorithm</b> - algorithm to find minimum spanning tree in an undirected weighted graph in <i>O(|E|log|V|)</i> time [<a href="prim.py">code</a>][<a href="https://en.wikipedia.org/wiki/Prim%27s_algorithm">wiki</a>][<a href="https://archive.org/details/bstj36-6-1389">paper</a>]</li>
  <li><b>Kruskal's Algorithm</b> - algorithm to find minimum spanning tree (or forrest) in an undirected weighted graph in <i>O(|E|log|V|)</i> time [<a href="kruskal.py">code</a>][<a href="https://en.wikipedia.org/wiki/Kruskal%27s_algorithm">wiki</a>]</li>
</ul>

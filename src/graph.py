import networkx as nx
import matplotlib.pyplot as plt
import numpy
import math
from pqueue import Pqeue

class Graph:

    chars = {chr(n): n-97 for n in range(97, 97+26)}

    def __init__(self, size) -> None:
        self.size = size
        self.__edges = [[0 for _ in range(size)] for _ in range(size)]

    def edge(self, node1, node2, weight):
        if type(node1) == str:
            node1 = Graph.chars[node1]

        if type(node2) == str:
            node2 = Graph.chars[node2]

        self.__edges[node1][node2] = weight
        self.__edges[node2][node1] = weight

    def __str__(self):
        return self.__edges.__str__()

    def get_edges(self):
        edges = []
        for i in range(self.size):
            for j in range(self.size - i):
                if self.__edges[i][j] != 0:
                    edges.append(i, j, self.__edges[i][j])


    # def kruskal(self):
    #     self.get_edges()

    def neighbors(self, node):
        if type(node) == str:
            node = Graph.chars[node]

        arr = self.__edges[node]


    def prim(self, src):
        if type(src) == str:
            src = Graph.chars[src]

        if src >= self.size:
            print("invalid source node")
            return -1

        nodes = [(i, src, math.inf) for i in range(self.size)]
        nodes[src] = (src, None, 0)

        Q = Pqeue(nodes)
        MST = Graph(self.size)
        taken_nodes = set()

        while not Q.empty():
            node = Q.pop()
            taken_nodes.add(node[0])

            if node[1] != None:
                MST.edge(node[0], node[1], node[2])

            neighbors = self.__edges[node[0]]

            for i in range(len(neighbors)):
                if neighbors[i] != 0 and i not in taken_nodes:
                    Q.update((i, node[0], neighbors[i]))

        return MST






    def visualize(self):
        """
        Visualize a graph using the provided adjacency matrix.
        """
        # Create a graph object from the adjacency matrix
        array = numpy.array(self.__edges)
        node_labels = {i: chr(65 + i) for i in range(array.shape[0])}  # create alphabetic node labels
        G = nx.DiGraph(array)
        G = nx.relabel_nodes(G, node_labels)

        # Draw the graph using a spring layout
        pos = nx.spring_layout(G)
        # pos = nx.arf_layout(G)
        pos = nx.circular_layout(G)
        # pos = nx.fruchterman_reingold_layout(G)
        # pos = nx.shell_layout(G)
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color="blue")
        nx.draw(G, pos, with_labels=True)
        # Show the plot
        plt.show()




g = Graph(9)
# print(g)
g.edge('a', 'b', 4)
g.edge('a', 'h', 8)
g.edge('h', 'b', 11)
g.edge('c', 'b', 8)
g.edge('h', 'i', 7)
g.edge('c', 'i', 2)
g.edge('h', 'g', 1)
g.edge('i', 'g', 6)
g.edge('f', 'g', 2)
g.edge('c', 'f', 4)
g.edge('c', 'd', 7)
g.edge('d', 'f', 14)
g.edge('e', 'f', 10)
g.edge('d', 'e', 9)
# g.edge('h', 'g', 1)
mst = g.prim('a')
mst.visualize()
print(mst)
# print(g)
# g.visualize()

import networkx as nx
import matplotlib.pyplot as plt
import numpy
import math
from pqueue import Pqeue
from LL import LL, Node

class Graph:
    chars = {chr(n): n-97 for n in range(97, 97+26)}

    def __init__(self, size, directed: bool) -> None:
        self.size = size
        self.__directed = directed
        self.__adjacency = [LL() for _ in range(size)]

    def edge(self, node1, node2, weight):
        if type(node1) == str:
            node1 = Graph.chars[node1]

        if type(node2) == str:
            node2 = Graph.chars[node2]

        self.__adjacency[node1].insert(Node(value=node2, weight=weight))

        if not self.__directed:
            self.__adjacency[node2].insert(Node(value=node1, weight=weight))

    def __str__(self):
        return self.__adjacency.__str__()

    def prim(self, src):
        # from alphabet to index
        if type(src) == str:
            src = Graph.chars[src]

        # validate
        if src >= self.size:
            print("invalid source node")
            return -1

        # initialize Queue
        nodes = [(i, src, math.inf) for i in range(self.size)]
        nodes[src] = (src, None, 0)
        Q = Pqeue(nodes)

        # create empty MST graph
        MST = Graph(self.size, directed=True)

        # set to keep track of visited nodes
        taken_nodes = set()

        while not Q.empty():
            # get next node
            vertix = Q.pop()

            # mark it as visited
            taken_nodes.add(vertix[0])

            # if not first node then add edge to MST
            if vertix[1] != None:
                MST.edge(vertix[1], vertix[0], vertix[2])

            # get the out edges
            neighbors = self.__adjacency[vertix[0]]

            # iterate over edges
            node = neighbors.head
            while node != None:
                if node.value not in taken_nodes:
                    Q.update((node.value, vertix[0], node.weight))
                node = node.next

        return MST

    def dijkstra(self, src):
        shortest_path = Graph(self.size, directed= True)

        # from alphabet to index
        if type(src) == str:
            src = Graph.chars[src]

        # validate
        if src >= self.size:
            print("invalid source node")
            return -1

        vertices = [(i, None, math.inf) for i in range(self.size)]
        vertices[src] = (src, None, 0)
        Q = Pqeue(vertices)

        # taken_nodes = set()
        visited = [0 for _ in range(self.size)]

        while not Q.empty():
            # get next node
            vertix = Q.pop()

            # mark it as visited
            # taken_nodes.add(vertix[0])
            visited[vertix[0]] = vertix[2]

            # if not first node then add edge to MST
            if vertix[1] != None:
                shortest_path.edge(vertix[1], vertix[0], vertix[2]-visited[vertix[1]])

            # get the out edges
            neighbors = self.__adjacency[vertix[0]]

            # iterate over edges
            node = neighbors.head
            while node != None:
                # if node.value not in taken_nodes:
                if visited[node.value] == 0:
                    Q.update((node.value, vertix[0], node.weight+vertix[2]))
                node = node.next
        return shortest_path

    def visualize(self, root=0, block=True, title='', tree=False):

        plt.figure(title)
        adj_list = self.__adjacency
        # Create an empty graph
        if self.__directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        # Iterate over the linked lists and add the edges to the graph
        for i in range(len(adj_list)):
            curr = adj_list[i].head
            while curr:
                if self.__directed:
                    G.add_edge(chr(65 + i), chr(65 + curr.value), weight=curr.weight, arrowsize=12, arrowstyle='->')
                else:
                    G.add_edge(chr(65 + curr.value), chr(65 + i), weight=curr.weight)
                curr = curr.next

        # Draw the graph using NetworkX and Matplotlib
        if tree:
            pos = nx.nx_pydot.graphviz_layout(G, prog='dot', root=root)
        else:
            pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos, width=1)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        # plt.gcf().canvas.set_window_title(title)
        plt.axis('off')
        plt.show(block=block)


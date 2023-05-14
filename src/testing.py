from graph import Graph

# prim test
g = Graph(size=9, directed=False)
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


# dijkstra test
d = Graph(size=5, directed=True)

d.edge('a', 'b', 10)
d.edge('a', 'd', 5)
d.edge('b', 'c', 1)
d.edge('b', 'd', 2)
d.edge('d', 'b', 3)
d.edge('c', 'e', 4)
d.edge('e', 'c', 6)
d.edge('d', 'e', 2)
d.edge('d', 'c', 9)
d.edge('e', 'a', 7)

dij = d.dijkstra(0)
dij.visualize()

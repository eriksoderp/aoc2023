import networkx as nx
from math import prod

G = nx.Graph()
for l in open('input25.txt', 'r').readlines():
    node, neighbours = l.strip().split(':')
    G.add_edges_from((node, neighbour) for neighbour in neighbours.split())

G.remove_edges_from(nx.minimum_edge_cut(G))

print(prod(len(component) for component in list(nx.connected_components(G))))

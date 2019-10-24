import pydot
import networkx as nx
from itertools import permutations


def is_subgraph(big, small):
    big_permutation = list(permutations(big.nodes(), len(small.nodes())))
    print(big_permutation)
    
    for perm in big_permutation:
        sub_nodes = list(perm)
        sub_in_big = big.subgraph(sub_nodes)
        
        if(nx.is_isomorphic(sub_in_big, small_graph) == True):
            return True
        else:
            continue
        
        
        
"""

def main():
    big_graph = nx.drawing.nx_pydot.read_dot("data/basic_blocks_dot/Ap1Bigheights-CFG.dot")
    
    small_graph = nx.MultiDiGraph()
    small_graph.add_node(0)
    small_graph.add_node(1)
    small_graph.add_node(2)
    small_graph.add_edge(0, 1)
    small_graph.add_edge(0, 2)

    is_subgraph(big_graph, small_graph)


if __name__ == "__main__":
	main()

"""

import pydot
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


def is_subgraph(big, small):
    big_combination = list(combinations(big.nodes(), len(small.nodes())))
    #print(big_permutation)
    
    for comb in big_combination:
        sub_nodes = list(comb)
        sub_in_big = big.subgraph(sub_nodes)
        
        if(nx.is_isomorphic(sub_in_big, small) == True):
            print("It is a Subgraph!!")
            break
        
    # Draw two compared graphs
    fig = plt.figure(figsize=(5, 10))
    plt.subplot(2, 1, 1)
    nx.draw(big_graph)
    plt.title("bigger graph")

    plt.subplot(2, 1, 2)
    nx.draw(small_graph)
    plt.title("smaller graph") 
    
    plt.show()
        
	
####################################################################
# @unique_graph: unique sub-graph structures given the number of nodes
# return unique_graph
####################################################################
def find_unique_subgraph(num_node):
    print("Unique subgraphs with {} nodes".format(num_node))
    unique_graph = []

    for g in graphs: # traverse all graphs
        graph = g[0]

        graph_combination = combinations(graph.nodes(), num_node)
        for comb in graph_combination: # check all possible subgraphs
            sub_nodes = list(comb)
            sub_in_graph = graph.subgraph(sub_nodes)

            
            if not unique_graph: # empty list 
                unique_graph.append(sub_in_graph)
                print(graph.graph)
            else:
                index = 0
                for u_g in unique_graph: # not empty, comparison is needed
                    if(nx.is_isomorphic(u_g ,sub_in_graph)):
                        break
                    else:
                        index += 1
                     
                if(index == len(unique_graph)):
                    unique_graph.append(sub_in_graph)
                    print(graph.graph)
                    
    
    return unique_graph
	
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

    sub_graph_with_2_nodes = find_unique_subgraph(2)
    
if __name__ == "__main__":
	main()

"""

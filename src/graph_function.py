import pydotimport os
import pydot
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import classify_graph

####################################################################
# When two inputs 'big and small' are given, 
# check if the small graph is the subgraph of the big one.
####################################################################
def is_subgraph(big, small):
    big_combination = list(combinations(big.nodes(), len(small.nodes())))
    #print(big_permutation)
    
    for comb in big_combination:
        sub_nodes = list(comb)
        sub_in_big = big.subgraph(sub_nodes)
        
        if(nx.is_isomorphic(sub_in_big, small) == True):
            print("It is a Subgraph!!")
            return True
    
    """
    # Draw two compared graphs
    fig = plt.figure(figsize=(5, 10))
    plt.subplot(2, 1, 1)
    nx.draw(big)
    plt.title("bigger graph")

    plt.subplot(2, 1, 2)
    nx.draw(small)
    plt.title("smaller graph") 
    
    plt.show()
    """
    
    return False
        
    
####################################################################
# @unique_graph: unique sub-graph structures given the number of nodes
# return unique_graph
####################################################################
def find_unique_subgraph(graphs, num_node):
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
                print("new unique subgraph is in " + graph.graph['name'])
            else:
                index = 0
                for u_g in unique_graph: # not empty, comparison is needed
                    if(nx.is_isomorphic(u_g ,sub_in_graph)):
                        break
                    else:
                        index += 1
                     
                if(index == len(unique_graph)):
                    unique_graph.append(sub_in_graph)
                    print("new unique subgraph is in " + graph.graph['name'])
                    
    print("There are {} unique subgraph in input graph".format(len(unique_graph)))

    return unique_graph

####################################################################
# Read all kinds of subgraphs
####################################################################
def read_subgraphs():
    sub_graphs = []
    for id in range(27):
        sub_graph = nx.drawing.nx_pydot.read_dot("../data/subgraphs/index" + str(id) + ".dot")
        sub_graphs.append(sub_graph)


    return sub_graphs


####################################################################
# Check how many subgraphs exist on the graph
####################################################################
def contain_which_sub(graph):

    ####################################################################
    # Check how many times a subgraph appears on the graph
    ####################################################################
    def how_many_sub(graph, sub):

        count = 0
        combination = list(combinations(graph.nodes(), len(sub.nodes())))
        
        for comb in combination:
            sub_nodes = list(comb)
            sub_in_graph = graph.subgraph(sub_nodes)
            
            if(nx.is_isomorphic(sub_in_graph, sub) == True):
                print("Input subgraph is in the graph")
                count += 1

        return count
    ####################################################################

    sub_graphs = read_subgraphs()
    count_subs = []


    for sub in sub_graphs:
        count_subs.append(how_many_sub(graph, sub))

    print(count_subs)


####################################################################
# Get all graphs. There are 280 graphs in total.
####################################################################
def read_all_graphs(path):
    dot_files = os.listdir(path)
    
    graphs = []
    for f in dot_files:
        graphs.append(nx.drawing.nx_pydot.read_dot(path+ f))
        
    return graphs
        


####################################################################
# Divide graphs into two groups.
# One is the number of graphs with the subgraph and
# the other is the number of graphs without the subgraph
####################################################################
def split_graphs_by(sub, graphs):
    
    include     = 0
    not_include = 0
    
    for g in graphs:
        if(is_subgraph(g, sub) == True):
            include += 1
        else:
            not_include += 1
            
    return include, not_include

def main():
    """Test1: is_subgraph
    big_graph = nx.drawing.nx_pydot.read_dot("../data/basic_blocks/dot/Ap1Bigheights-CFG.dot")
    contain_which_sub(big_graph)
    small_graph = nx.MultiDiGraph()
    small_graph.add_node(0)
    small_graph.add_node(1)
    small_graph.add_node(2)
    small_graph.add_edge(0, 1)
    small_graph.add_edge(0, 2)

    is_subgraph(big_graph, small_graph)
    """

    """Test2: find_unique_subgraphs
    graphs = classify_graph.classify_graph("../data/basic_blocks/json/")

    find_unique_subgraph(graphs, 4) 

    """

    """Test3: split_graphs_by_subgraph
    all_graphs = read_all_graphs("../data/basic_blocks/dot/")
    subs = read_subgraphs()
    split_graphs_by(subs[23], all_graphs)
    """
    

if __name__ == "__main__":
	main()

import os
import json
import networkx as nx

def classify_graph(json_files):

    graph_types = []
    # Traverse all graphs
    for file in json_files:
        print(file)
        
        with open(path + file, 'r') as f:
            data = json.load(f)
    
        graph = make_nxgraph(file, data['nodes'], data['edges'])
    
        is_classified = 0
        
        for i in range(len(graph_types)):
            if (nx.is_isomorphic(graph_types[i][0], graph)):
                graph_types[i].append(graph)
                is_classified = 1

        if(is_classified == 0):
            graph_types.append([graph])


    return graph_types

    
def make_nxgraph(file, nodes, edges):
    
    nxgraph = nx.MultiDiGraph(name = file)
    
    for n in nodes:
        nxgraph.add_node(n['id'])
    for e in edges:
        nxgraph.add_edge(e['source'], e['target'])

    
    return nxgraph
    
    
def main():
	path = "data/basic_blocks/"
	json_files = os.listdir(path)
	

if __name__ == "__main__":
	main()

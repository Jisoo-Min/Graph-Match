import os
import json
import math
import networkx as nx
import matplotlib.pyplot as plt

def classify_graph(path):

    json_files = os.listdir(path)
    
    graph_types = []
    # Traverse all graphs
    for file in json_files:
        
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

    print("The number of classes: ", len(graph_types))
    
    
    return graph_types

    
def make_nxgraph(file, nodes, edges):
    
    nxgraph = nx.MultiDiGraph(name = file)
    
    for n in nodes:
        nxgraph.add_node(n['id'])
    for e in edges:
        nxgraph.add_edge(e['source'], e['target'])

    
    return nxgraph

def class_distribution(graphs):

    plt.figure(figsize=(18, 5))

    plt.bar(range(len(graphs)), [len(i) for i in graphs])

    plt.show()

def draw_class(class_num, graphs):
    class_num = int(class_num)
    class_size = len(graphs[class_num])


    print("Now drawing >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Size: ", class_size)

    counter = 0

    fig = plt.figure(class_num, figsize=(10, 7))

    while(counter < class_size ):
        subplot_size = math.sqrt(class_size) + 1
        sub_plot = fig.add_subplot(subplot_size, subplot_size, counter+1)
        sub_plot.set_title(graphs[class_num][counter].graph['name'], fontsize = 4.5)
        nx.spring_layout(graphs[class_num][counter], weight='length')
        nx.draw(graphs[class_num][counter], node_size = 5, arrowsize = 8)
        counter += 1

    plt.subplots_adjust(hspace= 1, wspace=0.35)
    plt.show()

    
def main():
    graphs = classify_graph("data/basic_blocks_json/")
    print("Class distribution")
    class_distribution(graphs)
	
    quit = ['q', 'Q']

    user_input = input("If you want see each class, write the class number. If not, press Q")
    while( not(str(user_input) in quit)):
        draw_class(user_input, graphs)

        user_input = input("If you want see each class, write the class number. If not, press Q")


if __name__ == "__main__":
	main()

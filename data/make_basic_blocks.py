import os
import json
import ntpath
import pprint
from sys import argv
from collections import Counter

def make_basic_blocks(input_file, output_type):
	
	with open (input_file, "r") as f:
		data = json.load(f)

	# Get nodes and edges
	nodes = data['nodes']
	edges = data['edges'] 

	print("Start with default nodes")
	print("now nodes: ",  [list(d.values())[0] for d in nodes])

	cycle = 1     # Check cycle 
	pointer = 0   # It works as pointer in a list
	alternative_node = 1 # When new node is inserted, use this as a node id

	# Traverse nodes
	while(pointer < len(nodes)):
		# get node in nodes list
		print("\n\nIn cycle: ", cycle)
		cycle += 1
		print("Which node is now selected: "),
		pprint.pprint(nodes[pointer]['label']), 
		###################################################################
		# Get general information

		# Get node 
		node = nodes[pointer]
	    # Get node's id 
		node_id = node['id']
	    
	    # Find source and target nodes
		s_nodes = [list(d.values())[1] for d in edges]
		d_nodes = [list(d.values())[2] for d in edges]

		# Count frequency of source/target nodes
		count_s_nodes = Counter(s_nodes)
		count_d_nodes = Counter(d_nodes)

	    # Find nodes which have multiple children(branches)
		multi_child_nodes  = [node for node, frequecny in count_s_nodes.items() if frequecny > 1]
	    # Find nodes which have multiple parents
		multi_parent_nodes = [node for node, frequecny in count_d_nodes.items() if frequecny > 1]
		##################################################################

	    # If the number of node's branches is not 1, cannnot merge.

	    # Traverse all source nodes
		if(node_id in s_nodes): 
			"""
			1. If the number of node's branches is not 1, cannnot merge.
			2. If the child node has multiple parent nodes, cannot merge.
			"""

			# Count the number of child nodes(branches) to check conditions
			child_of_node  = [(child['target']) for idx, child in enumerate(edges) if child['source'] == node['id']]
	        
			# condition 1) If the node has multiple branches, cannot merge with the child nodes. 
			# e.g. When node is an "if statement"
			if(len(child_of_node) != 1): # Cannnot merge
				pointer += 1 			 # Move pointer
				continue

			# (condition 2) If the node has only one child, check condition 2
			else: 
				child_id = child_of_node[0] # Get the child's id
				# For loop statements are here! -> multiple parents nodes
				if(child_id in multi_parent_nodes): # If child node has multiple parent nodes, cannot merge
					pointer += 1					# Move pointer
					continue

				 # Can merge!! 
				else:
					"""
					1. In nodes, Remove two nodes.
					2-1. Merge two nodes -> alternative node (new node)
					2-2. Add alternative node (new node) into node list.
					3-1. Remove a edge which connects two nodes
					3-2. In edges, Change all node ID to new node ID.
					"""

	                # Copy node, and delete it
					tmp_node = node     
					del nodes[pointer]
	               
	                # Find child node, and delete it
					tmp_child_idx, tmp_child = [(idx, child) for idx, child in enumerate(nodes) if child['id'] == child_id][0]
					del nodes[tmp_child_idx]

					# Create new node (merged node), and insert it in nodes
					new_node = {
						'id': ('a' + str(alternative_node)),
						'line': str(tmp_node['line']) + "-"  + str(tmp_child['line']),
						'label': tmp_node['label'] + "\t" + tmp_child['label'],
						}
					nodes.insert(pointer, new_node)

			
	                
	                # Find a edge which connects two nodes, and delete it
					tmp_edge_idx, tmp_edge = [(idx, edge) for idx, edge in enumerate(edges) 
	                                          if ((edge['source'] == tmp_node['id']) and (edge['target'] == tmp_child['id']))][0]
					del edges[tmp_edge_idx]
	                

	                # In edges, modify node ID as alternative node ID (new noe ID)
					for (i, e) in enumerate(edges):
						if(e['source'] == tmp_child['id']):
							edges[i]['source'] = 'a' + str(alternative_node)
						if(e['target'] == tmp_child['id']):
							edges[i]['target'] = 'a' + str(alternative_node)
						if(e['source'] == tmp_node['id']):
							edges[i]['source'] = 'a' + str(alternative_node)
						if(e['target'] == tmp_node['id']):
   							edges[i]['target'] = 'a' + str(alternative_node)    
	                        
	                # After add new node, update alternative node number        
					alternative_node += 1
	                
		else: # It is not one of the source node, and it is the last node with no branch.
			pointer += 1

		print("now nodes: ",  [list(d.values())[0] for d in nodes])
		print("now edges: ", [list(d.values())[0] for d in edges])

	print("\n FINISHED")


	javafile_name = ntpath.basename(input_file)
	if (output_type == 'dot'):
		dot_writer(javafile_name, nodes, edges)
	elif (output_type == 'json'):
		json_writer(javafile_name, nodes, edges)


def json_writer(file_name, nodes, edges):

	result_file = open('./basic_blocks/json/' + file_name[:-5] + ".json", "w+")
	data = {
		'file' : file_name[:-5] + ".java",
		'nodes': nodes,
		'edges': edges
	}
	
	json.dump(data, result_file, indent=4)

	result_file.close()
            
def dot_writer(file_name, nodes, edges):

    result_file = open("./basic_blocks/dot/" + file_name[:-5] + ".dot", 'w+')
    result_file.write("digraph " + "result_test { \n" +
                  "// graph-vertices\n")
    for n in nodes:
        node_id = n['id']
        node_label = str(n['line']) + ":  " + n['label']
        
        node_label = node_label.replace("\"", "'")
        result_file.write("  " + str(node_id) + "  [label=\"" +  node_label + "\"]; \n")

    result_file.write("// graph-edges\n")
    
    for e in edges: 
        edge_id = e['id']
        edge_label = e['label']
        edge_source = e['source']
        edge_target = e['target']
    
        result_file.write("  " + str(edge_source) + " -> " + str(edge_target) + "")
    
        if(edge_label == ""):
            result_file.write(";\n")
        else:
            result_file.write("  [label=\"" + edge_label + "\"]; \n")

    result_file.write("}")
    result_file.close()





def main():

	input_file  = argv[1]
	output_type = argv[2]

	if(output_type == "json"):
		if not os.path.exists("basic_blocks/json"):
			os.makedirs("basic_blocks/json")
	elif(output_type == "dot"):
		if not os.path.exists("basic_blocks/dot"):
			os.makedirs("basic_blocks/dot")



	make_basic_blocks(input_file, output_type)



if __name__ == "__main__":
	main()

#!/usr/bin/env python3
__description__ = \
"""

"""
__author__ = "Coralie Capron"
__date__ = "22.10.2019"

import argparse
import networkx as nx
import os
import statistics

def arg_parser():
    Parser = argparse.ArgumentParser(
        description="This script was written in the purpose ")

    Parser.add_argument('i', metavar='FASTQ_SE',
                        help='Fastq file single end')
    Parser.add_argument('k', metavar='KMERS_LENGTH',
                        help='The kmers length', type = int, default =21)
#    Parser.add_argument('r', metavar='REF_GENOME',
 #                       help='Reference genome', nargs='?')
    Parser.add_argument('o', metavar='CONFIG_FILE',
                        help='Config file')
    Args = Parser.parse_args()

    # print(Args.i.split(".")[1])
    # if Args.i.split(".")[1] != "fq":
    #     print(Args.i)
    #     raise ValueError("File is not a fastq file")
    # else:
    fastq_file = Args.i
    kmers_length = Args.k
    config_file = Args.o

    return (fastq_file,kmers_length, config_file)

def read_fastq(fastq_file):
	"""Open file and retrieve only the sequences in fastq file"""
    with open(fastq_file,"r") as file:
        for line in file:
            yield next(file).strip() #cut the \n at the end
            next(file)
            next(file)

def cut_kmer(seq, kmers_length):
	"""For each sequence, retrieve the kmers associated"""
	#We only need the kmers with a given length and not the smaller one
    for i in range(0,(len(seq)-kmers_length+1)):
        yield seq[i:i+kmers_length]

def build_kmer_dict(fastq_file,kmers_length):
	""" Create a dict with the kmers in a seq and their \
	occurences."""
    dict_kmer={}
    for seq in read_fastq(fastq_file):
        for kmer in cut_kmer(seq, kmers_length):
            if kmer not in dict_kmer.keys():
                dict_kmer[kmer] = 1
            else:
                dict_kmer[kmer] += 1
    return dict_kmer

def build_graph(dict_kmer):
	"""Create a graph with nodes and edges with the kmers"""
    graphe = nx.DiGraph() #Creates an oriented graph
    for key in dict_kmer.keys():
        graphe.add_edge(key[:-1],key[1:],weight=dict_kmer[key])
    return(graphe)

def get_starting_nodes(graphe):
	""" Get the nodes without any ancestors/predecessor"""
    entry_node_list = []
    for node in graphe.nodes():
    	#pred, retrieves the predecessors
        if len(graphe.pred[node]) == 0: 
            entry_node_list.append(node)
    return(entry_node_list)

def get_sink_nodes(graphe):
	"""Get the nodes without any descending/successors"""
    exit_node_list = []
    for node in graphe.nodes():
        if len(graphe.succ[node]) == 0:
            exit_node_list.append(node)
    return (exit_node_list)

def get_contigs(graphe,starting_list, exit_node_list):
    list_tuple = []
    for start in starting_list:
        for exit in exit_node_list:
            for path in nx.all_simple_paths(graphe,start, exit):
                contig = path[0]
                for i in range(1,len(path)):
                    contig += path[i][-1]
                list_tuple.append((contig,len(contig)))
    return list_tuple

def fill(text, width=80):
    """Split text with a line return to respect fasta format"""
    return os.linesep.join(text[i:i+width] for i in range(0, len(text), width))


def save_contigs(list_tuple,out):
    i = 0
    with open(out,"w") as output:
        for tuple in list_tuple:
            frst_line =">contig_"+str(i)+" len="+str(tuple[1])+"\n"
            seq = fill(tuple[0])
            output.write(frst_line)
            output.write(seq+"\n")
            i += 1

def std(list_values):
    return statistics.stdev(list_values)

def path_average_weight(graphe, path):
    list_weight =[]
    for u,v,e in graphe.subgraph(path).edges(data=True):
        list_weight.append(e["weight"])
    return statistics.mean(list_weight)

def remove_paths(graphe, list_path, delete_entry_node, delete_sink_node):
    for path in list_path:
        if (delete_entry_node == True and delete_sink_node == True):
            graphe.remove_nodes_from(path)
        elif (delete_entry_node == True and delete_sink_node == False):
            graphe.remove_nodes_from(path[0:-1])
        elif (delete_entry_node == False and delete_sink_node == True):
            graphe.remove_nodes_from(path[1:])
        elif (delete_entry_node == False and delete_sink_node == False):
            graphe.remove_nodes_from(path[1:-1])
    return(graphe)

def select_best_path(graphe, list_path, list_long_path,list_av_weight, delete_entry_node=False, delete_sink_node=False):
    max_weight = max(list_av_weight)
    max_index=[i for i, weight in enumerate(list_av_weight) if weight== max_weight]
    # Retrieve path with max average weight and their indexes
    #if there is more than one
    if len(max_index)>1:
    	max_index_path = [list_long_path[i] for i in max_index]
    	max_len_path=max(max_path)
    	if len(max_len_path)>1:
    		random.seed(9001)
    		random.randint(1,len(max_len_path))


    		
    	# max_path=[i for i, weight in enumerate(list_av_weight) if weight== max_weight]
     #    max_length = 0
     #    for index in max_index:
     #    	#amongst the index with max weight, the one with the longest paths:
     #        if (liste_long_path[index] > max_length):
     #            max_length = liste_long_path[index]
     #        elif liste_long_path[elt] == max_length:


            else:



    else:
        best_path=list_path[i]





def solve_bubble():
    pass


def simplify_bubbles():
    pass


def solve_entry_tips():
    pass


def solve_out_tips():
    pass

def main():
    fastq_file,kmers_length, config_file = arg_parser()
    dict_kmer= build_kmer_dict(fastq_file,kmers_length)
    graphe = build_graph(dict_kmer)
    list_start = get_starting_nodes(graphe)
    list_end = get_sink_nodes(graphe)
    list_tuple = get_contigs(graphe,list_start, list_end)
    out= "contigs.fasta"
    save_contigs(list_tuple,out)
    remove_paths(graphe, list_path, delete_entry_node, delete_sink_node)

if __name__ == "__main__":
    main()

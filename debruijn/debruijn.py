#!/usr/bin/env python3
__description__ = \
"""

"""
__author__ = "Coralie Capron"
__date__ = "22.10.2019"

import argparse
import networkx as nx

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
    with open(fastq_file,"r") as file:
        for line in file:
            yield next(file).strip()
            next(file)
            next(file)

def cut_kmer(seq, kmers_length):
    for i in range(0,(len(seq)-kmers_length+1)):
        yield seq[i:i+kmers_length]

def build_kmer_dict(fastq_file,kmers_length):
    dict_kmer={}
    for seq in read_fastq(fastq_file):
        for kmer in cut_kmer(seq, kmers_length):
            if kmer not in dict_kmer.keys():
                dict_kmer[kmer] = 1
            else:
                dict_kmer[kmer] += 1
    return dict_kmer

def build_graph(dict_kmer):
    graphe = nx.DiGraph()
    for key in dict_kmer.keys():
        graphe.add_edge(key[:-1],key[1:],weight=dict_kmer[key])
    return(graphe)

def get_starting_nodes(graphe):
    entry_node_list = []
    for node in graphe.nodes():
        if len(graphe.pred[node]) == 0:
            entry_node_list.append(node)
    return(entry_node_list)
def std():
    pass


def get_sink_nodes(graphe):
    exit_node_list = []
    for node in graphe.nodes():
        if len(graphe.succ[node]) == 0:
            exit_node_list.append(node)
    return (exit_node_list)

def get_contigs(graphe,starting_list, exit_node_list):




def path_average_weight():
    pass


def remove_paths():
    pass


def select_best_path():
    pass


def save_contigs():
    pass




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
    print(list_start)
    print(list_end)
if __name__ == "__main__":
    main()

#!/usr/bin/env python
__description__ = \
"""

"""
__author__ = "Coralie Capron"
__date__ = "22.10.2019"

import argparse
import networkx

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

    if Args.i.split(".")[1] != "fq":
        print(Args.i)
        raise ValueError("File is not a fastq file")
    else:
        fastq_file = Args.i
    kmers_length = Args.k
    config_file = Args.o

    return (fastq_file,kmers_length, config_file)

def read_fastq(fastq_file):
    with open(fastq_file,"r") as file:
        for line in file:
            yield next(file)
            next(file)
            next(file)

def cut_kmer(list_seq, kmers_length):
    for seq in list_seq:
        for i in range(len(seq)):
            if len(seq[i:i+kmers_length]) != kmers_length:
                break
            else:
                yield seq[i:i+kmers_length]

def build_kmer_dict(fastq_file,kmers_length):
    dict_kmer={}
    list_seq = [x[:-1] for x in read_fastq(fastq_file)]
    for kmer in cut_kmer(list_seq, kmers_length):
        if kmer not in dict_kmer.keys():
            dict_kmer[kmer] = 1
        else:
            dict_kmer[kmer] += 1
    return dict_kmer

def build_graph(dict_kmer):
    for key in dict_kmer.keys():
        graph = networkx.add_edge(key[:-1],key[1:],weight=dict_kmer[key])

def main():
    fastq_file,kmers_length, config_file = arg_parser()
    dict_kmer= build_kmer_dict(fastq_file,kmers_length)
    build_graph(dict_kmer)


if __name__ == "__main__":
    main()

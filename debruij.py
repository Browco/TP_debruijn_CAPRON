#!/usr/bin/env python
__description__ = \
"""

"""
__author__ = "Coralie Capron"
__date__ = "22.10.2019"

import argparse



def arg_parser():
    Parser = argparse.ArgumentParser(
        description="This script was written in the purpose ")

    Parser.add_argument('i', metavar='FASTQ_SE',
                        help='Fastq file single end')
    Parser.add_argument('k', metavar='KMERS_LENGTH',
                        help='The kmers length', default =21)
#    Parser.add_argument('r', metavar='REF_GENOME',
 #                       help='Reference genome', nargs='?')
    Parser.add_argument('o', metavar='CONFIG_FILE',
                        help='Config file')
    Args = Parser.parse_args()

    if Args.i.split(".")[1] != "fastq":
        print(Args.pdbfile)
        raise ValueError("File is not a fastq file")
    else:
        fastq_file = Args.i
    kmers_length = Args.k
    config_file = Args.o

    return (fastq_file,kmers_length, config_file)

def main():
    fastq_file,kmers_length, config_file = arg_parser()








if __name__ == "__main__":
    main()

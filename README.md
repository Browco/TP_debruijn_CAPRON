# TP_debruijn_CAPRON

This script was created in the purpose of transform a given 
fastq file to a De Bruijn graphe.

## Requirements

* Python 3.x (>3.4 , 3.7.4 precisely )
* Some Python modules : argparse, networkx, os, statistics, random
* Some tools : pytest, pylint


## Utilization

In a shell : 
```
python3 debruijn.py [-h] FASTQ_SE KMERS_LENGTH OUTPUT_FILE
```

Knowing that :
- FASTQ_SE : A fastq file single end
- KMERS_LENGTH : Create k-mers of a given length, by default = 21
- OUTPUT_FILE : Name of the contigs output file

## Output

This script will, for now, create a contigs file. 

# TP_debruijn_CAPRON
## Author : Coralie Capron


 > **Note to Diderot Bioinformatics Master students looking at this repository :**  
 > 
 > Bonjour à tous, vous avez accès ici à un repo que j'ai laissé en public pour évaluation en premier lieu puis en guise de démonstration du travail que j'ai pu faire lors de mon M2 par la suite. Vous avez donc la possibilité en tant qu'étudiant de regarder et/ou de cloner ce repo. A savoir toutefois que, bien que ce repo puisse vous inspirer (ou non) ou vous aider pour avancer dans votre travail, celui-ci est soumis à la propriété intellectuelle. A savoir donc que : Le plagiat, selon son niveau de gravité, est une contrefaçon. L'article L122-4 du Code de la propriété intellectuelle prévoit que "toute représentation ou reproduction intégrale ou parielle faite sans le consentement de l'auteur ou de ses ayants droit ou ayants cause est illicite". Soyez critique sur ce que vous trouverez dans ce repository, et dans les résultats qui y sont produits. Aidez-vous de ce travail mais par pitié, ne le plagiez pas bêtement, vous devez vous casser la tête pour devenir ensuite de bons bioinformaticiens. A bon entendeur. 

## Aim of this project

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

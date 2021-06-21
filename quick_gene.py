#! /usr/bin/env python3


print(r"""\

`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
   `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
     y==/        y==/        y==/        y==/
   ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
                """)

print('QuickGene v. 1.0.0')
print('Copyrights: Lukasz Sitko')
print('Contact: sitkolukasz98@gmail.com')

import argparse
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def run(args):
    with open(args.input, 'r') as filename:
        x = str(filename.readlines()[1:])
        x = x.upper()

    blast_query = NCBIWWW.qblast('blastn', 'nt', x)

    with open("my_blast.xml", "w") as save_to:
        save_to.write(blast_query.read())
        blast_query.close()

    blast_results = open("my_blast.xml", 'r')
    blast_record = NCBIXML.read(blast_results)

    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('e value:', hsp.expect)
            print('Score:', hsp.score)
            print('Alignment length:', hsp.align_length)
            print('Identities', hsp.identities)
            print('           ')


#Second part

    out = [(x[i:i+1]) for i in range(0, len(x), 1)]

#Base pairs count

    A=out.count('A')
    T=out.count('T')
    G=out.count('G')
    C=out.count('C')

#Output of sequence nucleotides composition

    print('Composition of A: ', A)
    print('Composition of T: ', T)
    print('Composition of G: ', G)
    print('Composition of C: ', C)

#Start and stop codons, number of putative coding sequences

    out1 = [(x[i:i+3]) for i in range(0, len(x), 3)]

    start_codon=out1.count('ATG')
    stop_codon_1=out1.count('TAA')
    stop_codon_2=out1.count('TAG')
    stop_codon_3=out1.count('TGA')

    stop_codons=stop_codon_1+stop_codon_2+stop_codon_3


    if start_codon>stop_codons:
        start_codon=stop_codons

    print('Number of start codons:', start_codon)
    print('Number of stop codons:', stop_codons)

def main():
	parser=argparse.ArgumentParser(description="Performs BLASTN search on input .fasta sequence")
	parser.add_argument("-in",help=".fasta input file" ,dest="input", type=str, required=True)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()

#Choose between input methods: user input / file 

x=input(str('Enter you sequence: '))

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

print('Start codons:', start_codon)
print('Stop codons:', stop_codons)


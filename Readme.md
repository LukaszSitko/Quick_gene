Quick gene is utility, which allows for DNA/RNA sequence similarity searches using BLASTN Api.

Dependencies:
- Python 3.0 or higher
- Argparse, available at: https://docs.python.org/3/library/argparse.html
- Biopython, avilable at: https://biopython.org/

Input file needs to be in '.fasta' format, it is preferred for sequence to start and finish in 2nd line.

Script needs to be made executable: 
chmod +x quick_gene.py

In order to run:
./quick_gene.py -in input_file.fasta 

my_blast.xml file with raw data will be created in execution folder, parsed output will be displayed in terminal, however can be saved to file by:
./quick_gene.py -in input_file.fasta > output_file.txt

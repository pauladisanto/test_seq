import Bio
from Bio.Seq import Seq

# Define a function to read the FASTA file removing \n
def read_file(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

# Read the FASTA file
filename = "dna_seq.txt"
fasta_file = read_file(filename)


#Convert the FASTA file to a dictionary containing sequence name as key and the sequence string as value
fasta_dict = {}
fasta_label = ""
for line in fasta_file:
    if '>' in line:
        fasta_label = line 
        fasta_dict[fasta_label] = ""
    else:
        fasta_dict[fasta_label] += line


for seq_name in fasta_dict:
    print(f"\n Analysis for sequence {seq_name}:")
    seq = Seq(fasta_dict[seq_name])
    print(len(seq))

    print(f"The reverse complement is:")
    print(seq.reverse_complement())

    print(f"The transcript is:")
    messenger_rna=seq.transcribe()
    print(messenger_rna)

    print(f"The protein is:")
    protein_from_rna=seq.translate()
    print(protein_from_rna)


import sys

def read_fasta(file):
    sequences = {}
    with open(file, 'r') as f:
        name = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences

def nexus_header(sequences):
    ntax = len(sequences)
    nchar = len([seq for seq in sequences.values()][0])
    return f"#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX={ntax} NCHAR={nchar};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX"


def nexus_body(sequences):
    body = ""
    for name, seq in sequences.items():
        body += f"{name}    {seq}\n"
    #print(body + "\nEND;")
    return body + "\nEND;"

if __name__ == "__main__":
    fasta_file = sys.argv[1]
    sequences = read_fasta(fasta_file)
    print(nexus_header(sequences))
    print(nexus_body(sequences))

















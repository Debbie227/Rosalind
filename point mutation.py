##Calculates the point mutations between two fasta sequences from a single file.

from Bio import SeqIO


def point_mut(a, b):
    mutation = 0
    index = 0
    for n in a:
        if n != b[index]:
            mutation += 1
            index += 1
        else:
            index += 1
    return mutation


sequence = []
with open('Fasta.txt') as file:
    for record in SeqIO.parse(file, "fasta"):
        sequence.append(record.seq)

print(point_mut(sequence[0], sequence[1]))

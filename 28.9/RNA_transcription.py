#Given a DNA strand, return its RNA complement (per RNA transcription).

dna = raw_input("Enter a DNA strand : ")
print dna[2]
for i in range(0, len(dna) - 1):
    if dna[i] == 'G':
        dna[i] = 'C'
    elif dna[i] == 'c':
        dna[i] = 'G'
    elif dna[i] == 'T':
        dna[i] = 'A'
    elif dna[i] == 'A':
        dna[i] = 'U'
print dna

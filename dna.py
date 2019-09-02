def DNA_strand(dna):
    side_dna = []
    print(dna)
    for i in dna:
        if i == 'A':
            side_dna.append('T')
        elif i == 'T':
            side_dna.append('A')
        elif i == 'C':
            side_dna.append('G')
        elif i == 'G':
            side_dna.append('C')
    print(side_dna)
    return ''.join(side_dna)
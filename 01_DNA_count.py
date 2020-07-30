DNA ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

A=0
T=0
C=0
G=0
for i in DNA:
    if i == 'A':
        A += 1
    if i == 'T':
        T += 1
    if i == 'G':
        G += 1
    if i == 'C':
        C += 1

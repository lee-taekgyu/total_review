DNA = 'AAAACCCGGT'
d_RNA = {'A':'T','T':'A','G':'C','C':'G'}

TEMPLATE = []

for i in range(len(DNA)):
    TEMPLATE.append(d_RNA[DNA[i]])
print(''.join(TEMPLATE))

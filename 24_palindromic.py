#sequence = input("INSERT : ")

base = {'A':'T','T':'A','C':'G','G':'C'}

TEMP = []
if len(sequence) % 2 == 0:
    for i in sequence:
        TEMP.append(base[i])
    TEMP = ''.join(TEMP)
    if sequence == TEMP[::-1]:
        print("Palindromic sequence - even") 
    else:
        print("Not Palindromic sequence - even")
elif len(sequence) % 2 == 1:
    for i in sequence:
        TEMP.append(base[i])
    TEMP = ''.join(TEMP)
    if sequence[0:int(len(sequence)/2)] == TEMP[int(len(TEMP)/2)+1:][::-1] and sequence[int(len(sequence)/2)+1:] == TEMP[:int(len(TEMP)/2)][::-1]:
        print("Palindromic sequence - odd")
    else:
        print("Not Palindromic sequence - odd")

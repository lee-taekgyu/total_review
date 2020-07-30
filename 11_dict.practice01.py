Sentence = 'we tried list and we tried dicts also we tried Zen'

l = Sentence.split(" ")
print(l)
counter = {}

for i in l:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)



import collections
cnt = collections.Counter(l)
print(cnt)

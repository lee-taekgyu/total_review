with open("./shortSentence00.txt", "w") as handle00:
    with open("./longsentence.txt", "r") as handle01:
        a = []
        for line in handle01:
            a.append(line)
        for i in range(len(a)):
            if i % 2 == 1:
                handle00.write(a[i])

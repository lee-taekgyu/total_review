f = open("./new.txt", 'w')
for i in range(1,11):
    data = "%d line.\n" %i
    f.write(data)
f.close()

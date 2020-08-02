a = int(input("INSERT :"))
b = int(input("INSERT :"))

cnt = 0
for i in range(0,10001):
    if i >= a and i <= b:
        if i % 2 == 1:
            cnt += i
print(cnt)

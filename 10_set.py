a = {1,2,3,4,5}
b = {1,3,5,7,9}

print(a & b)
print(a | b)
print(a ^ b)

a |= {100}
print(a)
a.update({200})
print(a)

a.add(999)
a.add(1000)
print(a)
a.remove(200)
print(a)
a.add(998)
print(a)

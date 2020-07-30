waiting = [1,2,3,4,5]

print("welcome {} client!".format(waiting.pop(0)))
print(waiting)
waiting.append(6)
waiting.append(waiting[-1] + 1)
print(waiting)
print(waiting.pop(3))



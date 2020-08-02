chicken = 10

def countChicken(people):
    chicken = 20
    chicken -= people
    print(f"{chicken} chicken remained")

def countChicken_global(people):
    global chicken
    chicken -= people
    print(f"{chicken} chicken remained")

print(chicken)
countChicken(5)
print(chicken)

print(chicken)
countChicken_global(5)

try:
    dan = int(input("INSERT : "))
    for i in range(1,10):
        if 2<= dan <= 9:
            print(i * dan)
    if dan > 9: 
        print("Too Much")
except ValueError:
    print("Check your num")

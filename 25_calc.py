first = input("FIRST INSERT :")
second = input("SECOND INSERT :")
opp = input("INSERT OPPERATOR :")

def calc(first, second, opp):
    result = eval(first+opp+second)
    return result
print(calc(first, second, opp))

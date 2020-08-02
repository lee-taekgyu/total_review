f_list= [0,1]

n = int(input("INSERT :"))

def FIVO(n):
    if n == 0:
        return f_list[0]
    elif n == 1:
        return f_list[1]
    elif n > 1:
        for i in range(n-2):
            f_list.append(f_list[-1] + f_list[-2])
        return f_list[n-1]

print(FIVO(n))


d = {'USD':'1,203.82', 'EUR':'1,365.73', 'JPY': '11.22', 'CNY':'172.04'}

num = float(input("Write your money :"))
#nation = str(input("Write your nation : "))



for nation in d.keys():
    print(round(float(d[nation].replace(',','')))*int(num),"KRW")

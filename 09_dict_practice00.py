dic = {'regNum0':'951213-0000000', 'regNum1': '960125-0000000', 'regNum2':'970705-0000000'}
d_month = {1:'JAN', 2:'FEB', 3:'MAR',4:'APR',5:'MAR', 6:'JUN', 7:'JLY',8:'AUG', 9:'SEP',10:'OCT',11:'NOV', 12:'DEC'}

Num0 = dic['regNum0']
print(Num0)
a = Num0[2:4]
b = Num0[4:6]

print(a)
print(d_month[int(Num0[2:4])])

print(d_month[12] + "-" + a)

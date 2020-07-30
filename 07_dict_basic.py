d_basic = {'key0':3, 'key01':5, 1:2}
print(d_basic['key0'])
d_basic['key0'] = 100
print(d_basic)

print(d_basic['key0'])
print(d_basic.keys())
print(d_basic.get('key0'))
print('key0' in d_basic)

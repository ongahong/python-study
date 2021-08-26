







dict1 = dict()
dict1['name'] = 'ziyi'
dict1['age'] = '18'
# print(f'{dict1}-{type(dict1)}-{len(dict1)}')


# def myDef(**kwargs):
#     print(f'{kwargs}-{type(kwargs)}-{len(kwargs)}')
#     for key,value in kwargs.items():
#         print(f'{key}---{value}')



myLam = lambda a : a * a
print(myLam(7))

def myDef2(a,b):
    print(f'{a}-{type(a)}-{len(a)}')
    print(f'{b}-{type(b)}-{len(b)}')
    print(myLam(int(a)))

myDef2('5','10')









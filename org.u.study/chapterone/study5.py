

try:
    list1 = list()
    list1.append(123)
    for i in list1:
        print(list1[i + 1])
except Exception as e:
    print(f'异常:{e}')
else:
    a = '没有异常'
    print(f'异常:{a}')
finally:
    b = '最后执行'
    print(f'异常:{b}')

def def1(a,b):
    return a + b

print(def1(12,12))







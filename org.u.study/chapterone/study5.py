
#
# try:
#     list1 = list()
#     list1.append(123)
#     for i in list1:
#         print(list1[i + 1])
# except Exception as e:
#     print(f'异常:{e}')
# else:
#     a = '没有异常'
#     print(f'异常:{a}')
# finally:
#     b = '最后执行'
#     print(f'异常:{b}')
#
# def def1(a,b):
#     return a + b
#
# print(def1(12,12))
#
#
# # 计算黄金分割数列的值
# def fn(n):
#     if n <= 1:
#         return n
#     else:
#         return fn(n - 1) + fn(n - 2)
#
# print(fn(4))

# 闭包
#
# list1 = list()
# list1.append(2)
# list1.append(3)
# result = 0
# print(f'start: list1:{list1}; result:{result}')
# for i in list1:
#     print(f'{list1.index(i)} --- {i}')
#     result += i
# print(f'end: list1:{list1}; result:{result}')
#
#
# print(f'2start: list1:{list1}; result:{result}')
# for i in range(0,len(list1)):
#     print(f'{i} --- {list1[i]}')
#     result += list1[i]
# print(f'2end: list1:{list1}; result:{result}')




# tuple1 = (2,3,4)
# print(tuple1)
# for i in tuple1:
#     print(f'fun:i:{tuple1.index(i)}---{i}')

#


def testKargs(*args):
    print(f'testKargs:args:{args}')
    return args

testKargs(1,2,3,4,5)


def outer(func):
    def inner(*args):
        # print(f'start.params:{args};params-type:{type(args)}')
        # print(f'start.params:{func.__name__}')
        func(args)
        print(f'end')
    return inner

@outer
def func (*args):
    print(f'fun:args:{args}')
    result = 0
    for i in args:
        #print(f'fun:i:{args.index(i)}---{i}')
        result += i

    print(f'fun:result:{result}')
    return result

func(1,2,3,4,5)








#第一题
outCount = 0
def outer():
    a = outCount
    def inner():
        nonlocal a
        a += 1
        print(a)
        return a
    print(a)
    return inner

print(outer())




# 第二题
# def sumOut(func):
#     print('现在开始求 1 到 n 的累计和，环境已准备就绪！')
#     def sumInner(n):
#         return func(n)
#     return sumInner
#
# @sumOut
# def sum(n):
#     result = 0
#     for i in range(n):
#         result += i
#     return result
#
# print(f'{sum(5)} \n计算结束,你是否做对了呢？')

# 第三题
# class student:
#
#     def __init__(self,name,age,number):
#         self.name = name
#         self.age = age
#         self.number = number
#
#     def showStudy(self):
#         print(f'我叫{self.name}， 我今年{self.age}岁了， 我的学生编号是{self.number}，请大家多多关照' )
#
#
# student1 = student('张三',15,139940556)
# student1.showStudy()


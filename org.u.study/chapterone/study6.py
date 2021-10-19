# # 父类私有属性
# class A:
#
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#
#     def __test(self):
#         print(f'私有方法中：{self.num1},{self.__num2}')
#
#
#
# class B(A):
#     def demo(self):
#         print('哈哈')
#         # 子类不能直接访问父类的私有属性
#         # print('访问父类的私有属性%d' % self.__num2)
#         # 子类不能直接访问父类的私有属性
#         # self.__test()
# b = B()
# b.demo()
# print(b.__num2)
# b.__test()


class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print(f'私有方法中：{self.num1},{self.__num2}')

    # 添加公有方法
    def test(self):
        print(f'父类的私有属性{self.__num2}')
        self.__test()   # 在公有方法中调用私有方法

class B(A):
    def demo(self):
        print('哈哈')
b = B()
print(b.num1)
b.test()


list1 = list()
list1.append(1)
list1.append(2)
list1.append(3)

it = iter(list1)
print(it)
print(it.__next__())





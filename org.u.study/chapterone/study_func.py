


# 递归函数

# 求和 - 循环求和
def func_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    print(sum)

# 求和 - 递归求和
def func_sum_2(n):
    if n > 0 :
        return func_sum_2(n - 1) + n
    else:
        return 0

# 闭包函数实现计数功能
def mycount():
    icount = 0
    def inner():
        nonlocal icount  # 声明x为父级变量；保证变量不被销毁；存在函数内部
        icount += 1
        return icount
    return inner




# fun_count = mycount()
# print(fun_count())
# print(fun_count())
# print(fun_count())
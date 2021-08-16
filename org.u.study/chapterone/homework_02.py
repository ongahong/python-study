
# 1 编程题，求输入数的阶乘
num = int(input("请输入数字： "))
# print(f'输入的数字是：{num}')
result = 1
i = 1
while i <= num :
    result = result * i
    #     print(f'当前i:{i},当前result：{result}')4
    i+=1
print(f'输入的数字是：{num}; 阶乘是：{result}')


# 2 用户名 密码编程题，嵌套可以做太复杂了
nameFailCount = 0
passwordFailCount = 0
name = input("请输入姓名：")
password = input("请输入密码：")
if(nameFailCount >2 or passwordFailCount >2):
    print('限制了')
else:
    if(name == 'lucy'):
        if(password == '123456'):
            print("恭喜你，登录成功")
        else:
            passwordFailCount +=1
            print('密码错了')
    else:
        nameFailCount+=1
        name = input("请输入姓名：")
        password = input("请输入密码：")


# 3  统计字符数量
inputStr = input("请输入： ")
length = len(inputStr);
print(f'输入的字符串是：{inputStr}；字符串长度是：{length}')
i = 0
numCount = 0
daCount = 0
xiaoCount = 0
otherCount = 0

while i < length:
    temp = inputStr[i:i+1]
    print(temp)
    if(temp.islower()):
        xiaoCount+=1
    elif(temp.isupper()):
        daCount+=1
    elif(temp.isnumeric()):
        numCount+=1
    else: otherCount+=1
    i +=1

print(f'大写字符：{daCount} 小写字符：{xiaoCount} 数字：{numCount}  其他字符：{otherCount}')
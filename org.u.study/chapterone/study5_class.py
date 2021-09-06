
class study:

    name = ''
    age = 0
    sex = 0

    def __init__(self,name,sex,age):
        print(self)
        self.name = name
        self.age = age
        self.sex = sex

    # def __str__(self):
    #     print(self)

    def getUser(self):
        print('111111')
        return 0




study1 = study('mingming',3,1)
study1.getUser()
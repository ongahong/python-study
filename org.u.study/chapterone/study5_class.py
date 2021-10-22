

# 类，继承，单例

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
        print(f'{self.name}')
        print('111111')
        return 0

# study1 = study('mingming',3,1)
# study1.getUser()




class Father:
    def sing(self):
        print(f'{123}')

class Mother:
    def dance(self):
        print(f'{456}')

class Daughter(Mother,Father):
    def dance(self):
        super().dance()

    def attack(self):
        print("打架")


d = Daughter()
d.sing()
d.attack()
d.dance()


class signal(object):

    ins = None

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = object.__new__(cls)
        return cls.ins

signalEntity = signal('萝卜')
print(signalEntity)
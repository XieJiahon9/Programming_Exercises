#练习9.13 骰子：创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
#编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
#创建一个6面的骰子并掷10次。创建一个10面的骰子和一个20面的骰子，再分别掷10次。
from random import randint

class Die:
    """ 骰子 """
    def __init__(self, sides = 6):
        """ 初始化 """
        self.sides = sides
        self.result = 0

    def roll_die(self):
        """ 摇骰子 """
        self.result = randint(1, self.sides)
        return self.result


times = 10
die6 = Die();
while times > 0:
    result = die6.roll_die()
    print(result)
    times -= 1

print("----------------------------------")
times = 10
die10 = Die(10);
while times > 0:
    result = die10.roll_die()
    print(result)
    times -= 1

print("----------------------------------")
times = 10
die20 = Die(20);
while times > 0:
    result = die20.roll_die()
    print(result)
    times -= 1
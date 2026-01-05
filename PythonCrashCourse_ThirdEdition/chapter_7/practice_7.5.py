#练习7.5 电影票：有家电影院根据观众的年龄收取不同的票价：
#不到3岁的观众免费；3（含）～12岁的观众收费10美元；年满12岁的观众收费15美元。
#请编写一个循环，在其中询问用户的年龄，并指出其票价。
while True:
    age = int(input("How old are you?(Enter '0' to quit): "))

    if age == -1:
        break
    elif age < 3:
        print("The price of your age is free.")
    elif age < 12:
        print("The price of your age is 10 dollars.")
    else:
        print("The price of your age is 15 dollars.")

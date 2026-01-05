#练习7.6 三种出路：以不同的方式完成练习7.4或练习7.5，在程序中采取如下做法。
#在while循环中使用条件测试来结束循环。
#使用变量active来控制循环结束的时机。
#使用break语句在用户输入 'quit' 时退出循环。
#practice_7.5
#条件测试
age = int(input("How old are you?(Enter '0' to quit): "))
while age > 0:

    if age < 3:
        print("The price of your age is free.")
    elif age < 12:
        print("The price of your age is 10 dollars.")
    else:
        print("The price of your age is 15 dollars.")

    age = int(input("How old are you?(Enter '0' to quit): "))

#-----------------------------------------------------------------------
#active
active = True
while active:
    age = int(input("How old are you?(Enter '0' to quit): "))

    if age == 0:
        active = False
    elif age < 3:
        print("The price of your age is free.")
    elif age < 12:
        print("The price of your age is 10 dollars.")
    else:
        print("The price of your age is 15 dollars.")

#-----------------------------------------------------------------------
#break
while True:
    age = int(input("How old are you?(Enter '0' to quit): "))

    if age == 0:
        break
    elif age < 3:
        print("The price of your age is free.")
    elif age < 12:
        print("The price of your age is 10 dollars.")
    else:
        print("The price of your age is 15 dollars.")

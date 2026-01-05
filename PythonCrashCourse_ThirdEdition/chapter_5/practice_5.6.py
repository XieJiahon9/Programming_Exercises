#练习5.6 人生的不同阶段：设置变量age的值，再编写一个if-elif-else结构，根据age的值判断这个人处于人生的哪个阶段。
#如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
#如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
#如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
#如果年龄为13（含）～18岁，就打印一条消息，指出这个人是少年。
#如果年龄为18（含）～65岁，就打印一条消息，指出这个人是中青年人。
#如果年龄达到65岁，就打印一条消息，指出这个人是老年人。
age = int(input("Please input your age:")) #get age
if age < 2:
    print("This person is a baby!")
elif age < 13:
    print("This person is a child!")
elif age < 18:
    print("This person is a teenager!")
elif age < 65:
    print("This person is a middle-aged!")
else:
    print("This person is an elderly person!")

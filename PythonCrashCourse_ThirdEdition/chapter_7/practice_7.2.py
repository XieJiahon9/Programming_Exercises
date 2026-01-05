#练习7.2 餐馆订位：编写一个程序，询问用户有多少人用餐。
#如果超过8个人，就打印一条消息，指出没有空桌；否则指出有空桌。
number = int(input("How many people are there for dinnner: "))
#if number <= 0:
#    print("Please enter the correct number: ")
if number > 8:
    print("Sorry, we don't have enough tables available.")
else:
    print("Welcome, we are plenty of tables!")
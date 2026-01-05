#练习4.11 你的比萨，我的比萨：在你为练习4.1编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas，再完成如下任务。
#在原来的比萨列表中添加一种比萨。在列表friend_pizzas中添加另一种比萨。
#核实有两个不同的列表。为此，打印消息“My favoritepizzas are:”，再使用一个for循环来打印第一个列表；
#打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
pizzas = ["pepperoni pizza", "Bar pizza", "Margarita pizza"] #practice_4.1
for pizza in pizzas:
    #print(pizza.lower()) #打印名称
    print(f"I like {pizza}!") #打印包含名称的句子
print("\nI really love pizza!")

print("------------------------------------------------")

friend_pizzas = pizzas[:]
pizzas.append("pizza1")
friend_pizzas.append("pizza2")

print("My favoritepizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

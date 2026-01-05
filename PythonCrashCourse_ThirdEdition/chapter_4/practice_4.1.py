#练习4.1 比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for循环将每种比萨的名称打印出来。
#修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨都显示一行输出，如下所示。
#I like pepperoni pizza.
#在程序末尾添加一行代码（不包含在for循环中），指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性的句子，如下所示。
#I really love pizza!
pizzas = ["pepperoni pizza", "Bar pizza", "Margarita pizza"]
for pizza in pizzas:
    #print(pizza.lower()) #打印名称
    print(f"I like {pizza}!") #打印包含名称的句子
print("\nI really love pizza!")

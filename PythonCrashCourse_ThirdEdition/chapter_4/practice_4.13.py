#练习4.13 自助餐：有一家自助式餐馆，只提供5种简单的食品。请想出5种简单的食品，并将其存储在一个元组中。
#使用一个for循环将该餐馆提供的5种食品都打印出来。
#尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
#餐馆调整菜单，替换了两种食品。请编写一行给元组变量赋值的代码，并使用一个for循环将新元组的每个元素都打印出来。
foods = ("rice", "meat", "vegetable", "egg", "milk")
for food in foods:
    print(food)

#food[1] = "fish" #尝试修改元素

foods = ("rice", "meat", "vegetable", "fish", "fruit")
for food in foods:
    print(food)
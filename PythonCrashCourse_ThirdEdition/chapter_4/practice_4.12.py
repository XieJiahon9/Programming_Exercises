#练习4.12 使用多个循环：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。
#请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表都打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake'] #food.py
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

print("-------------------------------------")

food_lists = [my_foods, friend_foods] #两个(嵌套)for循环
for food_list in food_lists:
    for food in food_list:
        print(food)
    print()
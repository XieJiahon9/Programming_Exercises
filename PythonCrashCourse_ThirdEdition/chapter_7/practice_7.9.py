#练习7.9 五香烟熏牛肉卖完了：使用为练习7.8创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
#在程序开头附近添加这样的代码：先打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
#再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
#确认最终的列表finished_sandwiches中未包含'pastrami'。
print("The pastrami is sold out!")

sandwich_orders = ['Chacarero', 'pastrami','Chip Butty', 'pastrami', 'pastrami', 'Bocadillo De Tortilla', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        continue
    else:
        finished_sandwiches.append(sandwich)

print(f"\nThe final finished_sandwiches_list is: {finished_sandwiches}")
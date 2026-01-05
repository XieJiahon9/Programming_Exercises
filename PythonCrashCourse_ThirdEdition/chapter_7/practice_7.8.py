#练习7.8 熟食店：创建一个名为sandwich_orders的列表，其中包含各种三明治的名字，再创建一个名为finished_sandwiches的空列表。
#遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，如“I made your tuna sandwich.”，
#并将其移到列表finished_sandwiches 中。当所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['Chacarero', 'Chip Butty', 'Bocadillo De Tortilla']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print(f"\nThe final finished_sandwiches_list is: {finished_sandwiches}")
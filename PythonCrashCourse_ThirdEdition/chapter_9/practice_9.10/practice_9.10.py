#练习9.10 导入Restaurant类：将最新的Restaurant类存储在一个模块中。
#在另一个文件中导入Restaurant类，创建一个Restaurant实例，并调用Restaurant的一个方法，以确认import语句正确无误。
from Restaurant import Restaurant

restaurant = Restaurant('restaurantA', 'food1')
print(restaurant.number_served)

restaurant.number_served = 20
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)
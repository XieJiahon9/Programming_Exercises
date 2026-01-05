#练习9.4 就餐人数：
#在为练习9.1编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
#根据这个类创建一个名为restaurant的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印。
#添加一个名为set_number_served()的方法，用来设置就餐人数。调用这个方法并向它传递新的就餐人数，然后再次打印这个值。

#添加一个名为increment_number_served()的方法，用来让就餐人数递增。
#调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant:
    """ 餐馆基本信息 """
    def __init__(self, restaurant_name, cuisine_type):
        """ 初始化 """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """ 打印前述两项信息 """
        print(f"The restaurant's name is {self.restaurant_name}, the retaurant's type is {self.cuisine_type}.")


    def open_restaurant(self):
        """ 打印消息，指出餐馆正在营业 """
        print("This restaurant is opening!")


    def set_number_served(self, number):
        """ 传递新的就餐人数 """
        if number > 0:
            self.number_served = number
        else:
            print("The number is wrong!")


restaurant = Restaurant('restaurantA', 'food1')
print(restaurant.number_served)

restaurant.number_served = 20
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)



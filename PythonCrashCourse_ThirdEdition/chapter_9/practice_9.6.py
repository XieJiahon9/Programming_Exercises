#练习9.6 冰激凌小店：冰激凌小店是一种特殊的餐馆。
#编写一个名为 IceCreamStand 的类，让它继承你为练习9.1或练习9.4编写的Restaurant类。
#这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
#编写一个显示这些冰激凌口味的方法。创建一个IceCreamStand实例，并调用这个方法。
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


class IceCreamStand(Restaurant):
    """ 冰淇淋餐馆 """
    def __init__(self, restaurant_name, cuisine_type = 'icecream'):
        """ 初始化 """
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = 'Original'


    def choose_flavors(self, flavor_name):
        """ 指定口味 """
        self.flavor = flavor_name


    def show_flavors(self):
        """ 展示口味 """
        print(f"The icecream is {self.flavor} flavor.")


my_restaurant = IceCreamStand('QD')
my_restaurant.show_flavors()
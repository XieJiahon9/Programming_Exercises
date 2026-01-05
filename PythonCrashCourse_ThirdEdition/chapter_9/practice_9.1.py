#练习9.1 餐馆：创建一个名为Restaurant的类，为其__init__()方法设置两个属性：restaurant_name和cuisine_type。
#创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
#根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant:
    """ 餐馆基本信息 """
    def __init__(self, restaurant_name, cuisine_type):
        """ 初始化 """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """ 打印前述两项信息 """
        print(f"The restaurant's name is {self.restaurant_name}, the retaurant's type is {self.cuisine_type}.")


    def open_restaurant(self):
        """ 打印消息，指出餐馆正在营业 """
        print("This restaurant is opening!")


my_restaurant = Restaurant('HJX', 'fast food')
print(f"name: {my_restaurant.restaurant_name}, type: {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
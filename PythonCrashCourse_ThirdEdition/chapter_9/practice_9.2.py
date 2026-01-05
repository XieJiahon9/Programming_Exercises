#练习9.2 三家餐馆：根据为练习9.1编写的类创建三个实例，并对每个实例调用describe_restaurant()方法。
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


restaurant1 = Restaurant('A', 'food1')
restaurant2 = Restaurant('B', 'food2')
restaurant3 = Restaurant('C', 'food3')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
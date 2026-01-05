""" 餐馆类 """

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
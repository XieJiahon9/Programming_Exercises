#练习9.3 用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介中通常会有的其他几个属性。
#在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
#创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
class User:
    """ 用户类 """
    def __init__(self, first_name, last_name, age, gender):
        """ 初始化 """
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.age = age
        self.gender = gender


    def describe_user(self):
        """ 打印用户信息摘要 """
        print(
            f"name: {self.full_name}\n"
            f"age: {self.age}\n"
            f"gender: {self.gender}"
        )


    def greet_user(self):
        """ 个性化打招呼 """
        print(f"Hello, my name is {self.full_name}.")


xjh = User('Xie', 'Jiahong', 21, 'male')
xjh.describe_user()
xjh.greet_user()

#练习9.7 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为练习9.3或练习9.5完成编写的User类。
#添加一个名为privileges的属性，用来存储一个由字符串（如 "can add post"、"can deletepost"、"can ban user" 等）组成的列表。
#编写一个名为show_privileges()的方法，显示管理员的权限。创建一个Admin实例，并调用这个方法。
class User:
    """ 用户类 """
    def __init__(self, first_name, last_name, age, gender):
        """ 初始化 """
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0


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


    def increment_login_attempts(self):
        """ 增加登入次数 """
        self.login_attempts += 1


    def reset_login_attempts(self):
        """ 清空登入次数 """
        self.login_attempts = 0;


class Admin(User):
    """ 管理员 """
    def __init__(self, first_name, last_name, age, gender):
        """ 初始化 """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = ["can add post", "can deletepost", "can ban user"]


    def show_privileges(self):
        """ 展示权限 """
        for privilege in self.privileges:
            print(privilege)


admin = Admin('Xie', 'Jiahong', 21, 'male')
admin.show_privileges()
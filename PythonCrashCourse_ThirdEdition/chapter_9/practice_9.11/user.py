""" 用户类、权限、管理员类 """


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


class Privileges():
    """ 权限 """
    def __init__(self):
        """ 初始化 """
        self.privileges = ["can add post", "can deletepost", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """ 管理员 """
    def __init__(self, first_name, last_name, age, gender):
        """ 初始化 """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

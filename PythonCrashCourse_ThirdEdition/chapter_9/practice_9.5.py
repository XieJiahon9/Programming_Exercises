#练习9.5 尝试登录次数：
#在为练习9.3编写的User类中，添加一个名为login_attempts的属性。
#编写一个名为increment_login_attempts()的方法，用来将属性login_attempts的值加1。
#再编写一个名为reset_login_attempts() 的方法，用来将属性login_attempts的值重置为0。

#根据User类创建一个实例，再调用increment_login_attempts()方法多次。
# 打印属性login_attempts的值，确认它正确地递增了。
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为 0。
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


xjh = User('Xie', 'Jiahong', 21, 'male')
print(xjh.login_attempts)
xjh.increment_login_attempts()
print(xjh.login_attempts)
xjh.increment_login_attempts()
print(xjh.login_attempts)
xjh.increment_login_attempts()
print(xjh.login_attempts)
xjh.increment_login_attempts()
print(xjh.login_attempts)
print("--------reset--------")
xjh.reset_login_attempts()
print(xjh.login_attempts)
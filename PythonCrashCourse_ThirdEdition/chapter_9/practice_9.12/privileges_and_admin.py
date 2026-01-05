""" 权限、管理员类 """
import user

class Privileges():
    """ 权限 """
    def __init__(self):
        """ 初始化 """
        self.privileges = ["can add post", "can deletepost", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(user.User):
    """ 管理员 """
    def __init__(self, first_name, last_name, age, gender):
        """ 初始化 """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


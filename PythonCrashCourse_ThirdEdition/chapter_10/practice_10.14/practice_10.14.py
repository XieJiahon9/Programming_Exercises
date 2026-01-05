#练习10.14 验证用户：最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。
#我们应修改这个程序，以防当前用户并非上次运行该程序的用户。为此，在greet_user()中打印欢迎用户回来的消息之前，询问他用户名是否是对的。
#如果不对，就调用get_new_username()让用户输入正确的用户名。
from pathlib import Path
import json

def get_stored_userinfo(path):
    """ 如果存储了用户信息，就获取它 """
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None

def get_new_userinfo(path, name):
    """ 提示用户输入用户名 """
    userinfo = {}
    user_name = name
    userinfo['name'] = user_name
    user_age = int(input("How old are you? "))
    userinfo['age'] = user_age
    user_gender = input("What is your gender? ")
    userinfo['gender'] = user_gender
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def confirm_user(path, name):
    """ 验证用户信息 """
    userinfo = get_stored_userinfo(path)
    if userinfo and userinfo['name'] == name:
        return userinfo
    else:
        return None

def show_userinfo():
    """ 问候用户，并指展示信息 """
    name = input("What is your name? ")
    path = Path('userinfo.json')
    userinfo = confirm_user(path, name)
    if userinfo:
        print(f"hi,{userinfo['name']},these are your information:\n{userinfo}")
    else:
        userinfo = get_new_userinfo(path, name)
        print(f"We'll remember you information, {userinfo['name']}!")

show_userinfo()
#练习10.13 用户字典：示例remember_me.py只存储了一项信息——用户名。请扩展该示例，让用户同时提供另外两项信息，再将收集到的所有信息存储到一个字典中。
#使用json.dumps()将这个字典写入文件，并使用json.loads()从文件中读取它。打印一条摘要消息，指出程序记住了有关用户的哪些信息。
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

def get_new_userinfo(path):
    """ 提示用户输入用户名 """
    userinfo = {}
    user_name = input("What is your name? ")
    userinfo['name'] = user_name
    user_age = int(input("How old are you? "))
    userinfo['age'] = user_age
    user_gender = input("What is your gender? ")
    userinfo['gender'] = user_gender
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def show_userinfo():
    """ 问候用户，并指展示信息 """
    path = Path('userinfo.json')
    userinfo = get_stored_userinfo(path)
    if userinfo:
        print(f"hi,{userinfo['name']},these are your information:\n{userinfo}")
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember you information, {userinfo['name']}!")

show_userinfo()
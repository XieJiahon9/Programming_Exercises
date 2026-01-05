#练习5.9 处理没有用户的情形：在为练习5.8编写的程序中，添加一条if语句，检查用户名列表是否为空。
#如果为空，就打印如下消息。
#We need to find some users!
users_list = ["admin", "Wang", "Sun", "Xie", "Wu", "Zhang", "Yao"]
#del users_list[:] #用来删除列表所以元素来测试没有用户的情况
if users_list:
    for user_name in users_list:
        if user_name == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user_name}, thank you for logging in again.")
else:
    print("We need to find some users!")
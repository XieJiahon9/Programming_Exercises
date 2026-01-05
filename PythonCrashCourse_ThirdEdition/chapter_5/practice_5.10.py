#练习5.10 检查用户名：按照下面的说明编写一个程序，模拟网站如何确保每个用户的用户名都独一无二。
#创建一个至少包含5个用户名的列表，并将其命名为current_users。
current_users = ["Wang", "Sun", "Xie", "Wu", "Zhang", "Yao", "Chen", "Qiu"]
#再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也在列表current_users中。
new_user = ["Wang", "xie", "Zhou", "xi"]
#遍历列表new_users，检查其中的每个用户名是否已被使用。
#如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
#确保比较时不区分大小写。换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
#（为此，需要创建列表current_users的副本，其中包含当前所有用户名的全小写版本。）
current_users_lowecase = [user.lower() for user in current_users]
for user in new_user:
    if user.lower() in current_users_lowecase:
        print("Sorry, you need to input again without reduplication.")
    else:
        print("It's a new user name you can use!")

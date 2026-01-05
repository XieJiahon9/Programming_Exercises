#练习8.11 消息归档：修改为练习8.10编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。
#调用send_messages()函数后，将两个列表都打印出来，确认原始列表保留了所有的消息。
def show_messages(messages):
    """ 展示消息 """
    for message in messages:
        print(f"{message}")


def send_messages(messages, send_messages):
    """ 发送消息 """
    while messages:
        sended_message = messages.pop()
        send_messages.append(sended_message)


messages = ['Hello!', 'Oh no!', 'Why?', 'Thank you.']
send_message = []

send_messages(messages[:], send_message)
show_messages(messages)
print("-------------------------------------------")
show_messages(send_message)
#练习8.10 发送消息：在为练习8.9编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列表中。
#调用send_messages()函数，再将两个列表都打印出来，确认把消息移到了正确的列表中。
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

send_messages(messages, send_message)
show_messages(messages)
print("-------------------------------------------")
show_messages(send_message)
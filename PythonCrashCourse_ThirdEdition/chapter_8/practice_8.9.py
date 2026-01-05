#练习8.9 消息：创建一个列表，其中包含一系列简短的文本消息。
#将这个列表传递给一个名为show_messages()的函数，这个函数会打印列表中的每条文本消息。
def show_messages(messages):
    """ 展示消息 """
    for message in messages:
        print(f"{message}")


messages = ['Hello!', 'Oh no!', 'Why?', 'Thank you.']
show_messages(messages)
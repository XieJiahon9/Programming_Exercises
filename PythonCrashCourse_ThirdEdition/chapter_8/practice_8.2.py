#练习8.2 喜欢的书：编写一个名为favorite_book()的函数，其中包含一个名为 title 的形参。让这个函数打印一条像下面这样的消息。
#One of my favorite books is Alice in Wonderland.
#调用这个函数，并将一本书的书名作为实参传递给它。
def favorite_book(title):
    """ 最喜爱的书 """
    print(f"My favorate book is {title}!")


favorite_book('Alice in Wonderland')
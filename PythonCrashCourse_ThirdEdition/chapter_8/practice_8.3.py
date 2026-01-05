#练习8.3 T恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
#这个函数应该打印一个句子，简要地说明T恤的尺码和字样。
#先使用位置实参调用这个函数来制作一件T恤，再使用关键字实参来调用这个函数。
def make_shirt(size, text):
    """ 制造T恤 """
    print(f"The size of shirt is {size}, the text printed on the shirt is '{text}'.")


#位置实参
make_shirt('XL', 'Hello')
#关键字实参
make_shirt(text='Hi', size='XXL')
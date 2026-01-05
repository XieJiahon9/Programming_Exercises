#练习8.4 大号T恤：修改make_shirt()函数，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
#调用这个函数分别制作一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size, text='I love Python'):
    """ 制造T恤 """
    print(f"The size of shirt is {size}, the text printed on the shirt is '{text}'.")


#位置实参
make_shirt('Large')
#关键字实参
make_shirt(size='Medium')
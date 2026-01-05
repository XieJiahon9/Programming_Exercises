#练习8.8 用户的专辑：在为练习8.7编写的程序中，编写一个while循环，让用户输入歌手名和专辑名。
#获取这些信息后，使用它们来调用make_album()函数并将创建的字典打印出来。
#在这个while循环中，务必提供退出途径。
def make_albium(singer_name, album_name):
    """ 描述音乐专辑 """
    return {'singer':singer_name, 'album':album_name}


while True:
    sname = input(f"What's your favorite singer/band?(Enter 'q' to quit.): ")

    if sname== 'q':
        break

    album_name = input(f"Do u kown one of their album?(Enter 'q' to quit.): ")

    if album_name != 'q':
        album_info = make_albium(sname, album_name)
        print(album_info)
    else:
        break

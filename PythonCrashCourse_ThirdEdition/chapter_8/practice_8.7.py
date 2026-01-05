#练习8.7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手名和专辑名，并返回一个包含这两项信息的字典。
#使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
#给make_album()函数添加一个默认值为None的可选形参，以便存储专辑包含的歌曲数。
#如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_albium(singer_name, album_name):
    """ 描述音乐专辑 """
    return {'singer':singer_name, 'album':album_name}


album1 = make_albium('ImagineDrago', "LOOM")
album2 = make_albium('Marvin Gaye', "What's Going Onmatch")
album3 = make_albium('The Beach Boys', "Pet Sounds")

print(album1)
print(album2)
print(album3)

print("----------------------------------------------------------------")

def make_albium(singer_name, album_name, songs_number=None):
    """ 描述音乐专辑 """
    if songs_number == None:
        return {'singer': singer_name, 'album': album_name}
    else:
        return {'singer':singer_name, 'album':album_name, 'song_numer':songs_number}


album4 = make_albium('ImagineDrago', "LOOM", 10)
album5 = make_albium('Marvin Gaye', "What's Going Onmatch")

print(album4)
print(album5)
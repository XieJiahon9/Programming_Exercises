#练习6.2 喜欢的数1：使用一个字典来存储一些人喜欢的数。
#请想出5个人的名字，并将这些名字用作字典中的键。再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。
#打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_number = {'Hong':9, 'Huang':8, 'Lan':7, 'Cheng':6, 'Bai':5}
for name in favorite_number:
    print(f"{name}'s favotite color is {favorite_number[name]}")
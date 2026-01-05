#练习6.10 喜欢的数2：修改为练习6.2编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数打印出来。
favorite_number = {'Hong':9, 'Huang':8, 'Lan':7, 'Cheng':6, 'Bai':5}
for name in favorite_number:
    print(f"{name}'s favotite color is {favorite_number[name]}")

print("---------------------------------")

favorite_number = {
    'Hong':[9, 5, 954, 64],
    'Huang':[8, 12, 8431, 23],
    'Lan':[7, 34, 566, 734],
    'Cheng':[6, 73, 1, 943],
    'Bai':[5, 157, 94, 6432],
}
for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorate numbers are {numbers}")
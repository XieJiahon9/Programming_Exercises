#练习9.15 彩票分析：可以使用一个循环来理解中前述彩票大奖有多难。
#为此，创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
#请打印一条消息，报告执行多少次循环才中了大奖。
from random import choice

my_ticke = ['3', '9', '4', 'n', '5', 'i', 'l', '2', '1', '7', 'w', '0', '8', 'e', '6']

win_times = 0
while True:
    result = '' #每次清空result字符串
    win_times += 1 #计数

    times = 4
    while times > 0:
        result += choice(my_ticke)
        times -= 1

    #检测数字，防止循环过大
    if win_times % 1024 == 0:
        print(win_times)

    if result == 'win7':
        print("You win the Grand Prize!")
        print(f"The result is {result} and the times to win is {win_times}.")
        break
#练习5.3 外星人颜色1：假设玩家在游戏中消灭了一个外星人，请创建一个名为alien_color的变量，并将其赋值为'green'、'yellow'或'red'。
alien_color = 'green'

#编写一条if语句，测试外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。
if alien_color == 'green':
    print("Congratulations, you got 5 score!")

#编写这个程序的两个版本，上述条件测试在其中的一个版本中通过，在另一个版本中未通过（未通过条件测试时没有输出）。
alien_color = 'yellow'
if alien_color == 'yellow':
    print("\nCongratulations, you are right!")
if alien_color == 'red':
    print("\nCongratulations, you are right!")

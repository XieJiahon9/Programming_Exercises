#练习5.4 外星人颜色2：像练习5.3那样设置外星人的颜色，并编写一个if-else结构。
alien_color = 'green'

#如果外星人是绿色的，就打印一条消息，指出玩家因消灭该外星人获得了5分。
#如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
if alien_color == 'green':
    print("You got 5 score!")
else:
    print("Congratulations, you got 10 score!")

#编写这个程序的两个版本，在一个版本中将执行if代码块，在另一个版本中将执行else代码块。
alien_color = 'red'
if alien_color == 'green':
    print("\nYou got 5 score!")
else:
    print("\nCongratulations, you got 10 score!")

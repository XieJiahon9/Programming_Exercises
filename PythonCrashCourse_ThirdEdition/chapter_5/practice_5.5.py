#练习5.5 外星人颜色3：将练习5.4中的if-else结构改为if-elif-else结构。
#如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
#如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
#如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
#编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。
#version_1
print("Version_1:")
alien_color = 'green'  #alien is green
if alien_color == 'green':
    print("The alien is green, you got 5 score!")
elif alien_color != 'green':
    print("The alien is yellow, you got 10 score!")
else:
    print("The alien is red, you got 15 score!")

#version_2
print("\nVersion_2:")
alien_color = 'yellow'  #alien is yellow
if alien_color == 'green':
    print("The alien is green, you got 5 score!")
elif alien_color == 'yellow':
    print("The alien is yellow, you got 10 score!")
else:
    print("The alien is red, you got 15 score!")

#version_3
print("\nVersion_3:")
alien_color = 'red'  #alien is red
if alien_color == 'green':
    print("The alien is green, you got 5 score!")
elif alien_color == 'yellow':
    print("The alien is yellow, you got 10 score!")
else:
    print("The alien is red, you got 15 score!")
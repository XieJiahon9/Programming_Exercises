#练习12.5 按键：编写一个创建空屏幕的Pygame文件。
#在事件循环中，每当检测到pygame.KEYDOWN事件时都打印属性event.key。
#运行这个程序并按下不同的键，看看控制台窗口的输出，以便了解Pygame会如何响应。
import sys
import pygame

def check_events():
    """ 检查事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            print(event.key)
        elif event.type == pygame.KEYUP:
            print(event.key)


screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Project_12.5")

while True:
    check_events()

    screen.fill((255, 255, 255))
    pygame.display.flip()
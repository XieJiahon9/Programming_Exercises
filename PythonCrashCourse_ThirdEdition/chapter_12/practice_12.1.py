#练习12.1 蓝色的天空：创建一个背景为蓝色的Pygame窗口。
import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

screen = pygame.display.set_mode((250, 250))  # 创建一个50*50大小的pygame窗口
pygame.display.set_caption("Project_12.1")  # 设置窗口名称

while True:
    check_events()

    screen.fill((0, 0, 255))  #设置窗口颜色
    pygame.display.flip()  #显示屏幕

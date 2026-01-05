#练习12.2 游戏角色：找一幅你喜欢的游戏角色的位图图像或将一幅图像转换为位图。
#创建一个类，将该角色绘制到屏幕中央，
#并将该图像的背景色设置为屏幕的背景色或将屏幕的背景色设置为该图像的背景色。
import sys
import pygame

def _check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 屏幕设置
screen_with_role = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pracitce_12.2: screen_with_role")

role_image = pygame.image.load(                         # 获取图像
"Programming_Exercises/PythonCrashCourse_ThirdEdition"
"/chapter_12/practice_12.2/role.bmp"
)

# 图像及其显示设置
swr_rect = screen_with_role.get_rect()  # swr为screen_with_role的缩写
ri_rect = role_image.get_rect()  # ri为role_image的缩写
ri_rect.center = swr_rect.center

while True:
    _check_events()

    screen_with_role.fill((255, 255, 255))
    screen_with_role.blit(role_image, ri_rect)
    
    pygame.display.flip()
    
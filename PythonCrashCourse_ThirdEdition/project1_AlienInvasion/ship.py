""" 飞船类 """
import pygame

class Ship:
    """ 管理飞船的类 """

    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图片并且获取外接矩形
        self.image = pygame.image.load(
            'Programming_Exercises/PythonCrashCourse_ThirdEdition/' 
            'project1_AlienInvasion/images/spaceship.bmp'
        )
        self.rect = self.image.get_rect()

        # 新飞船出现的位置(屏幕底部中央)
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
        
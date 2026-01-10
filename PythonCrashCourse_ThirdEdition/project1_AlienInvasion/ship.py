""" 飞船类 """
import pygame

class Ship:
    """ 管理飞船的类 """

    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船图片并且获取外接矩形
        self.image = pygame.image.load(
            'Programming_Exercises/PythonCrashCourse_ThirdEdition/' 
            'project1_AlienInvasion/images/spaceship.bmp'
        )
        self.rect = self.image.get_rect()

        # 新飞船出现的位置(屏幕底部中央)
        self.rect.midbottom = self.screen_rect.midbottom

        # 在属性x中存储浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 飞船移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """ 根据移动标志调整飞船位置 """
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up ==True and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        
        # 根据self.x/y更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
        
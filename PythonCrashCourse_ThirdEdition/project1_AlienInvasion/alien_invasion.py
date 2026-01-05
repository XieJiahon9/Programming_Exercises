import sys  # 退出游戏模块
import pygame  # 开发游戏所需模块

from ship import Ship
from settings import Settings


class AlienInvasion:
    """ 外星人入侵游戏资源和行为 """

    def __init__(self):
        """ 初始化游戏并且创建游戏资源 """
        pygame.init()  # 初始化背景
        self.clock = pygame.time.Clock()  # 定义时钟用于控制帧数
        self.settings = Settings()

        # 创建显示窗口和设置窗口名称
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 参数为一个元组
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # self表示指向的是当前类(AlienInvasion类)的实例

    def run_game(self):
        """ 开始游戏主循环 """
        while True:
            # 侦听键盘鼠标事件
            self._check_events()
                    
            # 每次循环时重绘屏幕,并且刷新屏幕
            self._update_screen()

            self.clock.tick(60)  # 使循环每秒运行60次/60帧

    def _check_events(self):  # 将管理事件的代码改写为辅助方法(只在类内调用)
        """ 响应键盘和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):  #更新屏幕代码改写为辅助方法
        """ 绘制屏幕并且切换到新屏幕 """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()



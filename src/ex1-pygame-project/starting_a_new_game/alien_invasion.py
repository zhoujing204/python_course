import sys
import pygame
from ship import Ship

class AlienInvasion:
    
    def __init__(self):
        
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
        
        self.ship = Ship(self)
        
    def run_game(self):
        
        while True:
            
            self._check_events()
            self.ship.update()
            
            self._update_screen()
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        # 刷新游戏的窗口        
        pygame.display.flip()
        self.clock.tick(60)        
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key==pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key==pygame.K_LEFT:
                    self.ship.moving_left = False
            
if __name__ == '__main__':
    
    ai = AlienInvasion() # __init__ 函数被调用
    ai.run_game()
                    
        

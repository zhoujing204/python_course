import pygame

class Game:
    def __init__(self):
        self.player_x = 0
        self.player_y = 0



    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_x -= 1
            elif event.key == pygame.K_RIGHT:
                self.player_x += 1
            elif event.key == pygame.K_UP:
                self.player_y -= 1
            elif event.key == pygame.K_DOWN:
                self.player_y += 1

    def update(self):
        # 游戏逻辑更新
        pass
import pygame
import sys

class AlienInvasion:
    """Game Main Class"""

    def __init__(self):
        """init the game"""
        print("__init__")
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Game Main Loop"""
        print("run_game")
        while True:
            # handle user input
            for event in pygame.event.get():

                # quit the game event
                if event.type == pygame.QUIT:
                    sys.exit()

            # update the display
            pygame.display.flip()


if __name__ == '__main__':
    # start the game
    print("start main")
    ai = AlienInvasion()
    ai.run_game()
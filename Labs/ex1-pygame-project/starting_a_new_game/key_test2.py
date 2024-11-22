import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key Test 2")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Convert event.key to lowercase for comparison
            key_name = pygame.key.name(event.key).lower()
            print(f"{key_name} is pressed")

            # Now check the lowercase key name
            if key_name == 'q':
                running = False
            if key_name == 'w':
                print("W pressed")

    pygame.display.flip()

pygame.quit()
sys.exit()
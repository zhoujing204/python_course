import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key Event Debug")

# Font setup
font = pygame.font.Font(None, 36)
text_lines = []  # Store multiple lines of text

def add_text_line(line):
    """Add a new line of text and keep only the last 10 lines"""
    text_lines.insert(0, line)
    if len(text_lines) > 10:
        text_lines.pop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Print detailed information for key events
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # Break down the event information
            event_info = {
                'Event Type': pygame.event.event_name(event.type),
                'Key Name': pygame.key.name(event.key),
                'Key Code': event.key,
                'Unicode': f"'{event.unicode}'",
                'Mod': event.mod,
                'Scancode': event.scancode
            }

            # Create formatted string
            info_str = f"Key: {event_info['Key Name']} "
            info_str += f"(Code: {event_info['Key Code']}, "
            info_str += f"Unicode: {event_info['Unicode']}, "
            info_str += f"Scancode: {event_info['Scancode']})"

            add_text_line(info_str)

            # Print to console for debugging
            print("\nEvent Details:")
            for key, value in event_info.items():
                print(f"{key}: {value}")

    # Draw event information on screen
    screen.fill((255, 255, 255))
    y = 550  # Start from bottom
    for line in text_lines:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (10, y))
        y -= 30

    pygame.display.flip()

pygame.quit()
sys.exit()
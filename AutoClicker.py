import pygame
import time
import pyautogui

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  # Remove pygame.NOFRAME
pygame.display.set_caption("Autoclicker")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Set up variables
autoclick = False

# Allow the window to remain focused
pygame.display.set_allow_screensaver(True)

# Main loop 
running = True
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Check if the spacebar is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        autoclick = not autoclick

    # Draw instructions
    instructions_text = font.render("Press SPACE to toggle Autoclicker", True, BLACK)
    screen.blit(instructions_text, (20, 20))

    # Draw autoclick status
    autoclick_text = font.render("Autoclick: " + ("ON" if autoclick else "OFF"), True, BLACK)
    screen.blit(autoclick_text, (20, 60))

    # Check if autoclick is enabled
    if autoclick:
        pyautogui.click()  # Perform a mouse click using pyautogui

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()

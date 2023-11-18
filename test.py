import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pygame Buttons')

clock = pygame.time.Clock()

# Load the background image
background_img = pygame.image.load('background_image.jpg')
background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Load icon image
icon_img = pygame.image.load('icon.png')
icon_img = pygame.transform.scale(icon_img, (30, 30))  # Adjust the icon size as needed

# Function to create a button with rounded corners, icon, and text
def create_button(surface, color, x, y, width, height, text='', text_color=BLACK, font_size=20, icon=None, border_radius=8):
    pygame.draw.rect(surface, color, (x, y, width, height), border_radius=border_radius)
    
    if icon:
        surface.blit(icon, (x + 10, y + (height - icon.get_height()) / 2))  # Adjust icon position
    
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    surface.blit(text_surface, text_rect)

# Define functions for button clicks (same as before)
# ...

# Game loop
running = True
while running:
    window.fill(WHITE)
    
    # Draw the background image
    window.blit(background_img, (0, 0))
    
    # Create buttons with rounded corners, icon, and text
    button1_x, button1_y = 50, 50
    button_width, button_height = 200, 50
    create_button(window, RED, button1_x, button1_y, button_width, button_height, text='Button 1', icon=icon_img)
    
    # Other buttons and functionalities (similarly as before)
    # ...

    # Event handling (same as before)
    # ...
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

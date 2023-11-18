import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def create_button(surface, color, x, y, width, height, text='', text_color=BLACK, font_size=20, icon=None, border_radius=8):
    pygame.draw.rect(surface, color, (x, y, width, height), border_radius=border_radius)
    if icon:
        surface.blit(icon, (x + 10, y + (height - icon.get_height()) / 2))
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    surface.blit(text_surface, text_rect)

def create_button2(surface, color, x, y, width, height, text='', text_color=WHITE, font_size=20, icon=None, border_radius=8):
    pygame.draw.rect(surface, color, (x, y, width, height), border_radius=border_radius)
    if icon:
        surface.blit(icon, (x + 10, y + (height - icon.get_height()) / 2))
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    surface.blit(text_surface, text_rect)
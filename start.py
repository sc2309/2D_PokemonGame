import pygame
import sys
from pokemon_data import *
from buttons import *
from attack import *

WHITE = (255, 255, 255)

def start_game():
    # Initialize Pygame
    g_health, solar_beam_a, hyper_beam_a, earthquake_a, rock_slide_a = groudon_d()
    k_health, water_gun_a, hydro_pump_a, hydro_cannon_a, hyperbeam_a_k = kyogre_d()
    FPS = 60
    pygame.init()

    # Set up the screen
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("POKEMON | Land vs Water")
    clock = pygame.time.Clock()
    # Load the background image from the 'assets' folder
    background_image = pygame.image.load("C:/sarthak/py/myPython/src/MyProjects/2dPokemon/Assets/terrain4.JPG")  # Replace "background.jpg" with your image file
    background_image = pygame.transform.scale(background_image, (width, height))

    # Load sticker images with transparent backgrounds
    kyogre = pygame.image.load("C:/sarthak/py/myPython/src/MyProjects/2dPokemon/Assets/kyogre2.png").convert_alpha() # Replace "sticker1.png" with your image file
    groudon = pygame.image.load("C:/sarthak/py/myPython/src/MyProjects/2dPokemon/Assets/groudon2.png").convert_alpha()  # Replace "sticker2.png" with your image file

    # Scale sticker images if needed
    kyogre = pygame.transform.scale(kyogre, (200, 200))  # Adjust the size as needed
    groudon = pygame.transform.scale(groudon, (300, 300))  # Adjust the size as needed

    hyper_beam = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/hyper_beam2.png')
    hyper_beam = pygame.transform.scale(hyper_beam, (30, 30))

    solar_beam = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/solar_beam2.png')
    solar_beam = pygame.transform.scale(solar_beam, (30, 30))

    earthquake = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/earthquake2.png')
    earthquake = pygame.transform.scale(earthquake, (30, 30))
    
    rock_slide = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/rock_slide2.png')
    rock_slide = pygame.transform.scale(rock_slide, (30, 30))

    water_gun = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/water_gun2.png')
    water_gun = pygame.transform.scale(water_gun, (30, 30))

    hydro_pump = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/hydro_pump2.png')
    hydro_pump = pygame.transform.scale(hydro_pump, (30, 30))

    hydro_cannon = pygame.image.load('C:/sarthak/py/2dPokemon/Assets/hydro_cannon2.png')
    hydro_cannon = pygame.transform.scale(hydro_cannon, (30, 30))

    # Position for the stickers
    top_right = (width - kyogre.get_width(), 300)
    bottom_left = (20, (height - groudon.get_height()) - 50)
    print('groudon\'s health is',g_health)
    print('kyogre\'s health is',k_health)
    # Main loop
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        # Place stickers on the background image
        screen.blit(kyogre, top_right)
        screen.blit(groudon, bottom_left)
        
        button1_x, button1_y = 15, 5
        button_width, button_height = 175, 50
        button_color = (255,43,43)
        create_button(screen, button_color, button1_x, button1_y, button_width, button_height, text='Hyper Beam!', icon=hyper_beam)

        button2_x, button2_y = 200, 5
        create_button(screen, button_color, button2_x, button2_y, button_width, button_height, text='Solar Beam!', icon=solar_beam)

        button3_x, button3_y = 15, 60
        create_button(screen, button_color, button3_x, button3_y, button_width, button_height, text='Earthquake!', icon=earthquake)

        button4_x, button4_y = 200, 60
        create_button(screen, button_color, button4_x, button4_y, button_width, button_height, text='Rock Slide!', icon=rock_slide)
        
        button_color = (57,117,255)
        button5_x, button5_y = 425, 5
        create_button2(screen, button_color, button5_x, button5_y, button_width, button_height, text='Water Gun!', icon=water_gun)
        
        button6_x, button6_y = 615, 5
        create_button2(screen, button_color, button6_x, button6_y, button_width, button_height, text='Hydro Pump!', icon=hydro_pump)

        button7_x, button7_y = 425, 60
        create_button2(screen, button_color, button7_x, button7_y, button_width, button_height, text='Hydro Cannon!', icon=hydro_cannon)

        button8_x, button8_y = 615, 60
        create_button2(screen, button_color, button8_x, button8_y, button_width, button_height, text='Hyper Beam!', icon=hyper_beam)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Fill the screen with the background image
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button1_x < mouse_x < button1_x + button_width and button1_y < mouse_y < button1_y + button_height:
                    print('-30 HP')
                    attack = 'hyper beam'
                    k_health = damage_kyogre(k_health, solar_beam_a, hyper_beam_a, earthquake_a, rock_slide_a, attack)
                    print('Kyogre HP:',k_health)
                    if k_health <= 0:
                        print('Groudon Won!')
                        sys.exit()
                elif button2_x < mouse_x < button2_x + button_width and button2_y < mouse_y < button2_y + button_height:
                    print('-40 HP')
                    attack = 'solar beam'
                    k_health = damage_kyogre(k_health, solar_beam_a, hyper_beam_a, earthquake_a, rock_slide_a, attack)
                    print('Kyogre HP:',k_health)
                    if k_health <= 0:
                        print('Groudon Won!')
                        sys.exit()
                elif button3_x < mouse_x < button3_x + button_width and button3_y < mouse_y < button3_y + button_height:
                    print('-30 HP')
                    attack = 'earthquake'
                    k_health = damage_kyogre(k_health, solar_beam_a, hyper_beam_a, earthquake_a, rock_slide_a, attack)
                    print('Kyogre HP:',k_health)
                    if k_health <= 0:
                        print('Groudon Won!')
                        sys.exit()
                elif button4_x < mouse_x < button4_x + button_width and button4_y < mouse_y < button4_y + button_height:
                    print('-20 HP')
                    attack = 'rock slide'
                    k_health = damage_kyogre(k_health, solar_beam_a, hyper_beam_a, earthquake_a, rock_slide_a, attack)
                    print('Kyogre HP:',k_health)
                    if k_health <= 0:
                        print('Groudon Won!')
                        sys.exit()
                elif button5_x < mouse_x < button5_x + button_width and button5_y < mouse_y < button5_y + button_height:
                    print('-20 HP Kyogre')
                    attack = 'water gun'
                    g_health = damage_groudon(g_health, water_gun_a, hydro_pump_a, hydro_cannon_a, hyperbeam_a_k, attack)
                    print('Groudon HP:',g_health)
                    if g_health <= 0:
                        print('Kyogre Won!')
                        sys.exit()
                elif button6_x < mouse_x < button6_x + button_width and button6_y < mouse_y < button6_y + button_height:
                    print('-30 HP Kyogre')
                    attack = 'hydro pump'
                    g_health = damage_groudon(g_health, water_gun_a, hydro_pump_a, hydro_cannon_a, hyperbeam_a_k, attack)
                    print('Groudon HP:',g_health)
                    if g_health <= 0:
                        print('Kyogre Won!')
                        sys.exit()
                elif button7_x < mouse_x < button7_x + button_width and button7_y < mouse_y < button7_y + button_height:
                    print('-40 HP Kyogre')
                    attack = 'hydro cannon'
                    g_health = damage_groudon(g_health, water_gun_a, hydro_pump_a, hydro_cannon_a, hyperbeam_a_k, attack)
                    print('Groudon HP:',g_health)
                    if g_health <= 0:
                        print('Kyogre Won!')
                        sys.exit()
                elif button8_x < mouse_x < button8_x + button_width and button8_y < mouse_y < button8_y + button_height:
                    print('-30 HP Kyogre')
                    attack = 'hyper beam'
                    g_health = damage_groudon(g_health, water_gun_a, hydro_pump_a, hydro_cannon_a, hyperbeam_a_k, attack)
                    print('Groudon HP:',g_health)
                    if g_health <= 0:
                        print('Kyogre Won!')
                        sys.exit()
                else:
                    print('Error')
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)
    # Quit Pygame
    pygame.quit()

start_game()
import pygame
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)




# set the center of the rectangular object.
def draw_ui(screen,score):
    ...

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f'{int(score)}', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (60, 60)

    screen.blit(text, textRect)

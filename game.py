import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

back_img = pygame.image.load('img/pixil-frame-0 (2).png')
run = True
while run:
    screen.blit(back_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        pygame.display.update()

pygame.quit()

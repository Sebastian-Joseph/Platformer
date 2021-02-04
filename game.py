import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

x = 50
y = 50
width = 40
height = 60
velocity = 20
back_img = pygame.image.load('img/pixil-frame-0 (2).png')
run = True
while run:
    screen.blit(back_img, (0, 0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= velocity
    if keys[pygame.K_SPACE]:
        y -= velocity
    if keys[pygame.K_s]:
        y += velocity
    if keys[pygame.K_d]:
        x += velocity

    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

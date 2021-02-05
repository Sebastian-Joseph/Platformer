import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

x = 0
y = 577
width = 40
height = 60
velocity = 10
back_img = pygame.image.load('img/pixil-frame-0 (2).png')

isJump = False
jumpCount = 10

run = True
while run:
    screen.blit(back_img, (0, 0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > velocity:
        x -= velocity
    if keys[pygame.K_SPACE] and y > 250 - velocity:
        isJump = True
    if not (isJump):
        if keys[pygame.K_s] and y < 585 - velocity:
            y += velocity
        if keys[pygame.K_d] and x < 665 - velocity:
            x += velocity
    else:
        if jumpCount >= -10:
            y -= jumpCount ** 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

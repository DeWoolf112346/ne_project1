import pygame
import time
import random
from idk import  *

WIDTH = 700
HEIGHT = 640
mouse_pos = 1

speed = 2
pygame.init()
m_of = False
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bg_color = (0, 0, 255)
bg_speed = 1
fon4 = pygame.image.load('pic/fon4.png')
fon4_rect = fon4.get_rect()
fon4_rect.centerx = 350
fon4_rect.centery = 320
fon3 = pygame.image.load('pic/fon3.png')
fon3_rect = fon3.get_rect()
fon3_rect.centerx = 350
fon3_rect.centery = 320
fon2 = pygame.image.load('pic/fon2.png')
fon2_rect = fon2.get_rect()
fon2_rect.centerx = 350
fon2_rect.centery = 320
fon1 = pygame.image.load('pic/fon1.png')
fon1_rect = fon1.get_rect()
fon1_rect.centerx = 350
fon1_rect.centery = 320
fon = pygame.image.load('pic/fon.png')
fon_rect = fon.get_rect()
fon_rect.centerx = 350
fon_rect.centery = 320
image = pygame.image.load('pic/zombi.png')
image_rect = image.get_rect()
image_rect.centerx = 350
image_rect.centery = 320
image2 = pygame.image.load('pic/da.png')
image2_rect = image.get_rect()
image2_rect.centerx = 350
image2_rect.centery = 320

kp_p = 0
kp_r = 0
text_size1 = 100
text_size2 = 50
color = (0, 0, 250)
color1 = (169,164,55)
color2 = (78,134,25)
color3 = (25,32,134)
color4 = (178,101,251)

show_text = True
run = True
K_right = False
K_left = False
K_down = False
K_up = False

while run:
    mouse_pos = pygame.mouse.get_pos()
    # screen.fill(color)
    if kp_p <= 0:
        screen.blit(fon, fon_rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_begin_rect.collidepoint(mouse_pos):
                show_text = False
                m_of = True
            if text_exit_rect.collidepoint(mouse_pos):
                pygame == quit()
                run = False
            if event.button == 1:
                print('LKM')
            elif event.button == 2:
                print('kolosiko')
            if event.button == 3:
                print('PKM')
            elif event.button == 4:
                print('kolosiko vpered')
            elif event.button == 5:
                print('kolosiko nazad')

        if m_of == True:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    K_up = False
                if event.key == pygame.K_DOWN:
                    K_down = False
                if event.key == pygame.K_RIGHT:
                    K_right = False
                if event.key == pygame.K_LEFT:
                    K_left = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    speed = speed + 1
                if event.key == pygame.K_KP_MINUS:
                    speed = speed - 1
                if event.key == pygame.K_RIGHT:
                    K_right = True
                if event.key == pygame.K_LEFT:
                    K_left = True
                if event.key == pygame.K_UP:
                    K_up = True
                if event.key == pygame.K_DOWN:
                    K_down = True

        if event.type == pygame.QUIT:
            print('Выход')
            run = False

    if image_rect.y >= 640:
        kp_p += 1
        kp_r = 1
        image_rect.y = 1
    if image_rect.y <= 0:
        kp_p += 1
        kp_r = 2
        image_rect.y = 600
    if image_rect.x >= 700:
        kp_p += 1
        kp_r = 3
        image_rect.x = 1
    if image_rect.x <= 0:
        kp_p += 1
        kp_r = 4
        image_rect.x = 699

    if kp_r == 1:
        screen.blit(fon1, fon1_rect)
        screen.blit(fon1r, fon1r_rect)
    if kp_r == 2:
        screen.blit(fon2, fon2_rect)
        screen.blit(fon2r, fon2r_rect)
    if kp_r == 3:
        screen.blit(fon3, fon3_rect)
        screen.blit(fon3r, fon3r_rect)
    if kp_r == 4:
        screen.blit(fon4, fon4_rect)
        screen.blit(fon4r, fon4r_rect)


    if image_rect.x >= 350:
        screen.blit(image2, image2_rect)
    if K_right:
        image_rect.x = image_rect.x + speed
    if K_left:
        image_rect.x = image_rect.x - speed
    if K_up:
        image_rect.y = image_rect.y - speed
    if K_down:
        image_rect.y = image_rect.y + speed
    screen.blit(image, image_rect)
    if speed <= 0:
        speed = 1
    if speed >= 10:
        speed = 10
    if show_text == True:
        screen.blit(text, text_rect)
        screen.blit(text_exit, text_exit_rect)
        screen.blit(text_begin, text_begin_rect)
        if text_begin_rect.collidepoint(mouse_pos):
            screen.blit(text_begin_active, text_begin_rect)
        else:
            screen.blit(text_begin, text_begin_rect)

        if text_exit_rect.collidepoint(mouse_pos):
            screen.blit(text_exit_active, text_exit_rect)
        else:
            screen.blit(text_exit, text_exit_rect)
    if show_text == False:
        screen.blit(info_chet, info_chet_rect)
        screen.blit(info_menu, info_menu_rect)
    pygame.display.flip()
    time.sleep(0.01)
pygame.quit()

# image_rect.bottomleft - координаты нижнего левого угла
# image_rect.bottomright - координаты нижнего правого угла
# image_rect.topleft - координаты верхнего левого угла
# image_rect.topright - координаты верхнего правого угла
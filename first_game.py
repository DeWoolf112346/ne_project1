from pygame import *
import time
import pyglet
import random
from for_text import  *
from playsound import playsound
pygame.init()

pygame.mixer.music.load("music/fon_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

coin_sound = pygame.mixer.Sound('music/monetky_sbor.mp3')
pobeda_sound = pygame.mixer.Sound('music/pobeda_music.mp3')

WIDTH = 500
HEIGHT = 500


monetky_mojno_1 = True
monetky_mojno_2 = True
monetky_mojno_3 = True
monetky_mojno_4 = True
monetky_mojno_5 = True

monetky_hitbox_1 = True
monetky_hitbox_2 = True
monetky_hitbox_3 = True
monetky_hitbox_4 = True
monetky_hitbox_5 = True

screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption('LoL')

bro_stamina = 10
mony = 0

salut = pygame.image.load('pic/salut.png')
salut_rect = salut.get_rect()
salut_rect.centerx = 100
salut_rect.centery = 200

salut2 = pygame.image.load('pic/salut2.png')
salut2_rect = salut2.get_rect()
salut2_rect.centerx = 400
salut2_rect.centery = 200

sad = pygame.image.load("pic/sad.png")
sad_rect = sad.get_rect()
sad_rect.centerx = 250
sad_rect.centery = 250

shahta = pygame.image.load("pic/shahta.png")
shahta_rect = shahta.get_rect()
shahta_rect.centerx = 250
shahta_rect.centery = 250

plaj = pygame.image.load("pic/plaj.png")
plaj_rect = plaj.get_rect()
plaj_rect.centerx = 250
plaj_rect.centery = 250

bro2 = pygame.image.load("pic/denchik2.png")
bro2_rect = bro2.get_rect()
bro2_rect.centerx = 250
bro2_rect.centery = 200

menu_guy = pygame.image.load("pic/menu_aaaa.png")
menu_guy_rect = menu_guy.get_rect()
menu_guy_rect.centerx = 250
menu_guy_rect.centery = 250

monetka = pygame.image.load('pic/monetka.png')
monetka_rect = monetka.get_rect()
monetka_rect.centerx = 460
monetka_rect.centery = 30

monetky = pygame.image.load('pic/monetka.png')

dereviya = pygame.image.load('pic/dereviya.png')
dereviya_rect = dereviya.get_rect()
dereviya_rect.centerx = 250
dereviya_rect.centery = 250

fonager2 = pygame.image.load('pic/fonager2.png')
fonager2_rect = fonager2.get_rect()
fonager2_rect.centerx = 250
fonager2_rect.centery = 250

bro = pygame.image.load('pic/denchik.png')
bro_rect = bro.get_rect()
bro_rect.centerx = 250
bro_rect.centery = 200
bro_shift_speed = False
mouse_pos = 1
bro_mode = 2

cou = 0
con = 0
fon_igri = 2
setings_mojno = False
setings_active_button = False
creators_mojno = False
nazad_active_button = False
exit_menu_active_button = False
menu_active_button = False
creators_active_button = False
continu_mojno = False
bro_speed = 1
right_fon = False
down_fon = False
left_fon = False
center_fon = False
run = True
m_of = False

monetka_1 = True
monetka_2 = True
monetka_3 = True
monetka_4 = True
monetka_5 = True

coins_rect_x_1 = random.randint(25, 160)
coins_rect_y_1 = random.randint(200, 300)

coins_rect_x_2 = random.randint(350, 450)
coins_rect_y_2 = random.randint(200, 300)

coins_rect_x_3 = random.randint(25, 160)
coins_rect_y_3 = random.randint(350, 450)

coins_rect_x_4 = random.randint(350, 450)
coins_rect_y_4 = random.randint(350, 450)

coins_rect_x_5 = random.randint(225, 280)
coins_rect_y_5 = random.randint(350, 450)

monetkaa_1 = monetky
monetkaa_1_rect = monetkaa_1.get_rect()
monetkaa_1_rect.centerx = coins_rect_x_1
monetkaa_1_rect.centery = coins_rect_y_1

monetkaa_2 = monetky
monetkaa_2_rect = monetkaa_2.get_rect()
monetkaa_2_rect.centerx = coins_rect_x_2
monetkaa_2_rect.centery = coins_rect_y_2

monetkaa_3 = monetky
monetkaa_3_rect = monetkaa_3.get_rect()
monetkaa_3_rect.centerx = coins_rect_x_3
monetkaa_3_rect.centery = coins_rect_y_3

monetkaa_4 = monetky
monetkaa_4_rect = monetkaa_4.get_rect()
monetkaa_4_rect.centerx = coins_rect_x_4
monetkaa_4_rect.centery = coins_rect_y_4

monetkaa_5 = monetky
monetkaa_5_rect = monetkaa_5.get_rect()
monetkaa_5_rect.centerx = coins_rect_x_5
monetkaa_5_rect.centery = coins_rect_y_5

exit33 = False
show_text = True
K_right = False
K_left = False
K_down = False
scorer = 0
win = False
K_up = False
zanovo_f = False

while run:
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(fonager2, fonager2_rect)
    font = pygame.font.Font(None, 20)
    text_score = font.render('Счёт: ' + str(mony), True, 'black')
    # text_score = font.render(f'Счёт: {score}', True, 'black')
    screen.blit(text_score, (375, 25))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if zanovo_f:
                if zanovo_rect.collidepoint(mouse_pos):
                    mony = 0
                    m_of = True
                    pygame.mixer.music.play(-1)
            if exit33:
                if exit3_rect.collidepoint(mouse_pos):
                    run = False
                    pygame.quit()
            if setings_mojno == True:
                if setings_rect.collidepoint(mouse_pos):
                    setings_active_button = True

            if nazad_rect.collidepoint(mouse_pos):
                creators_active_button = False
                setings_active_button = False
            if continu_mojno == True:
                if continu_rect.collidepoint(mouse_pos):
                    menu_active_button = False
                    m_of = True
            if exit_menu_active_button == True:
                if exit2_rect.collidepoint(mouse_pos):
                    pygame == quit()
                    run = False

            if creators_mojno == True:
                if creators_rect.collidepoint(mouse_pos):
                    creators_active_button = True

            if nachalo_rect.collidepoint(mouse_pos):
                show_text = False
                m_of = True
            if menu_rect.collidepoint(mouse_pos):
                menu_active_button = True
            if exit_rect.collidepoint(mouse_pos):
                if show_text == True:
                    pygame == quit()
                    run = False
        if event.type == pygame.QUIT:
            run = False
        if m_of == True:
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RSHIFT:
                    bro_shift_speed = False
                if event.key == pygame.K_UP:
                    K_up = False
                if event.key == pygame.K_DOWN:
                    K_down = False
                if event.key == pygame.K_RIGHT:
                    K_right = False
                if event.key == pygame.K_LEFT:
                    K_left = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_active_button = True
                if event.key == pygame.K_RSHIFT:
                    bro_shift_speed = True
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
    if K_right:
        bro_mode = 2
        bro_rect.x = bro_rect.x + bro_speed
        bro2_rect.x = bro2_rect.x + bro_speed
    if K_left:
        bro_mode = 1
        bro_rect.x = bro_rect.x - bro_speed
        bro2_rect.x = bro2_rect.x - bro_speed
    if K_up:
        bro_rect.y = bro_rect.y - bro_speed
        bro2_rect.y = bro2_rect.y - bro_speed
    if K_down:
        bro_rect.y = bro_rect.y + bro_speed
        bro2_rect.y = bro2_rect.y + bro_speed

    if m_of == True:
        screen.blit(menu, menu_rect)
        if  menu_rect.collidepoint(mouse_pos):
            screen.blit(menu_active, menu_rect)
        else:
            screen.blit(menu, menu_rect)








    if bro_rect.y >= 521:
        bro_rect.y = -49
        bro2_rect.y = -49
    if bro_rect.y <= -50:
        bro_rect.y = 520
        bro2_rect.y = 520
    if bro_rect.x >= 521:
        bro_rect.x = -49
        bro2_rect.x = -49
    if bro_rect.x <= -50:
        bro_rect.x = 520
        bro2_rect.x = 520

    if m_of == True:
        if keys[pygame.K_w]:
            bro_rect.y = bro_rect.y - bro_speed
            bro2_rect.y = bro2_rect.y - bro_speed
        elif keys[pygame.K_a]:
            bro_mode = 1
            bro_rect.x = bro_rect.x - bro_speed
            bro2_rect.x = bro2_rect.x - bro_speed
        elif keys[pygame.K_s]:
            bro_rect.y = bro_rect.y + bro_speed
            bro2_rect.y = bro2_rect.y + bro_speed
        elif keys[pygame.K_d]:
            bro_mode = 2
            bro_rect.x = bro_rect.x + bro_speed
            bro2_rect.x = bro2_rect.x + bro_speed

    if bro_shift_speed == True:
        bro_speed = 2
    elif bro_shift_speed == False:
        bro_speed = 1
    if bro_stamina <= 0:
        bro_shift_speed == False

    if show_text == True:
        screen.blit(nazvanie, nazvanie_rect)
        screen.blit(exit, exit_rect)
        screen.blit(nachalo, nachalo_rect)
        if  nachalo_rect.collidepoint(mouse_pos):
            screen.blit(nachalo_active, nachalo_rect)
        else:
            screen.blit(nachalo, nachalo_rect)

        if exit_rect.collidepoint(mouse_pos):
            screen.blit(exit_active, exit_rect)
        else:
            screen.blit(exit, exit_rect)

    if monetky_mojno_1 == True:
        screen.blit(monetkaa_1, monetkaa_1_rect)
    if monetky_mojno_2 == True:
        screen.blit(monetkaa_2, monetkaa_2_rect)
    if monetky_mojno_3 == True:
        screen.blit(monetkaa_3, monetkaa_3_rect)
    if monetky_mojno_4 == True:
        screen.blit(monetkaa_4, monetkaa_4_rect)
    if monetky_mojno_5 == True:
        screen.blit(monetkaa_5, monetkaa_5_rect)

    if menu_active_button == False:
        exit_menu_active_button = False
        creators_mojno = False
        setings_mojno = False
        continu_mojno = False
        setings_active_button = False
        creators_active_button == False

    if creators_active_button == False:
        nazad_active_button == False
    if bro_mode == 2:
        screen.blit(bro, bro_rect)
    if bro_mode == 1:
        screen.blit(bro2, bro2_rect)
    screen.blit(monetka, monetka_rect)
    screen.blit(dereviya, dereviya_rect)

    if menu_active_button == True:
        monetky_mojno_1 = False
        monetky_mojno_2 = False
        monetky_mojno_3 = False
        monetky_mojno_4 = False
        monetky_mojno_5 = False
        exit_menu_active_button = True
        creators_mojno = True
        setings_mojno = True
        continu_mojno = True
        m_of = False
        screen.blit(menu_guy, menu_guy_rect)
        screen.blit(exit2, exit2_rect)
        screen.blit(setings, setings_rect)
        screen.blit(creators, creators_rect)
        screen.blit(continu, continu_rect)
        if exit2_rect.collidepoint(mouse_pos):
            screen.blit(exit2_active, exit2_rect)
        else:
            screen.blit(exit2, exit2_rect)
        if continu_rect.collidepoint(mouse_pos):
            screen.blit(continu_active, continu_rect)
        else:
            screen.blit(continu, continu_rect)
        if creators_rect.collidepoint(mouse_pos):
            screen.blit(creators_active, creators_rect)
        else:
            screen.blit(creators, creators_rect)
        if setings_rect.collidepoint(mouse_pos):
            screen.blit(setings_active, setings_rect)
        else:
            screen.blit(setings, setings_rect)

    if creators_active_button == True:
        nazad_active_button = True
        setings_mojno= False
        exit_menu_active_button = False
        continu_mojno = False
        screen.blit(menu_guy, menu_guy_rect)
        screen.blit(director, director_rect)
        screen.blit(programist, programist_rect)
        screen.blit(dizainer, dizainer_rect)
        screen.blit(sponsor, sponsor_rect)
        screen.blit(osobay_blagodarnost, osobay_blagodarnost_rect)
        screen.blit(scenarist, scenarist_rect)
        screen.blit(sozdately, sozdately_rect)
        if nazad_active_button == True:
            screen.blit(nazad, nazad_rect)
            if nazad_rect.collidepoint(mouse_pos):
                screen.blit(nazad_active, nazad_rect)
            else:
                screen.blit(nazad, nazad_rect)
    if setings_active_button == True:
        nazad_active_button = True
        continu_mojno = False
        screen.blit(menu_guy, menu_guy_rect)
        if nazad_active_button == True:
            screen.blit(nazad, nazad_rect)
            if nazad_rect.collidepoint(mouse_pos):
                screen.blit(nazad_active, nazad_rect)
            else:
                screen.blit(nazad, nazad_rect)
        exit_menu_active_button = False
        screen.blit(gromkost, gromkost_rect)
        screen.blit(nastroiki, nastroiki_rect)

    if monetky_hitbox_1:
        if bro_rect.collidepoint(coins_rect_x_1, coins_rect_y_1) or bro2_rect.collidepoint(coins_rect_x_1, coins_rect_y_1):
            monetky_mojno_1 = False
            monetky_hitbox_1 = False
            mony += 1
            coin_sound.play()

    if monetky_hitbox_2:
        if bro_rect.collidepoint(coins_rect_x_2, coins_rect_y_2) or bro2_rect.collidepoint(coins_rect_x_2, coins_rect_y_2):
            monetky_mojno_2 = False
            monetky_hitbox_2 = False
            mony += 1
            coin_sound.play()

    if monetky_hitbox_3:
        if bro_rect.collidepoint(coins_rect_x_3, coins_rect_y_3) or bro2_rect.collidepoint(coins_rect_x_3, coins_rect_y_3):
            monetky_mojno_3 = False
            monetky_hitbox_3 = False
            mony += 1
            coin_sound.play()

    if monetky_hitbox_4:
        if bro_rect.collidepoint(coins_rect_x_4, coins_rect_y_4) or bro2_rect.collidepoint(coins_rect_x_4, coins_rect_y_4):
            monetky_mojno_4 = False
            monetky_hitbox_4 = False
            mony += 1
            coin_sound.play()

    if monetky_hitbox_5:
        if bro_rect.collidepoint(coins_rect_x_5, coins_rect_y_5) or bro2_rect.collidepoint(coins_rect_x_5, coins_rect_y_5):
            monetky_mojno_5 = False
            monetky_hitbox_5 = False
            mony += 1
            coin_sound.play()
   #if win == True:
   #    pygame.mixer.music.pause()
    if win == False:
        if mony >= 5:
            win = True
            pobeda_sound.play()
    if mony >= 5:
        zanovo_f = True
        m_of = False
        exit33 = True
        mw = True
        screen.blit(pobeda, pobeda_rect)
        screen.blit(salut, salut_rect)
        screen.blit(salut2, salut2_rect)
        screen.blit(zanovo, zanovo_rect)
        screen.blit(exit3, exit3_rect)
        if zanovo_rect.collidepoint(mouse_pos):
            screen.blit(zanovo_active, zanovo_rect)
        if exit3_rect.collidepoint(mouse_pos):
            screen.blit(exit3_active, exit3_rect)
        K_up = False
        K_right = False
        K_down = False
        K_left = False


    pygame.display.flip()

pygame.quit()

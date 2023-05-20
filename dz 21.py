# import pygame
# import time
# import random
# from for_text2 import  *
# pygame.init()
#
# WIDTH = 500
# HEIGHT = 500
#
# bro_stamina = 10
# fantom_mojno = False
#
#
#
#
# sad = pygame.image.load("pic/sad.png")
# sad_rect = sad.get_rect()
# sad_rect.centerx = 250
# sad_rect.centery = 250
#
# shahta = pygame.image.load("pic/shahta.png")
# shahta_rect = shahta.get_rect()
# shahta_rect.centerx = 250
# shahta_rect.centery = 250
#
# plaj = pygame.image.load("pic/plaj.png")
# plaj_rect = plaj.get_rect()
# plaj_rect.centerx = 250
# plaj_rect.centery = 250
#
# bro2 = pygame.image.load("pic/bro2.png")
# bro2_rect = bro2.get_rect()
# bro2_rect.centerx = 250
# bro2_rect.centery = 200
#
# menu_guy = pygame.image.load("pic/menu_aaaa.png")
# menu_guy_rect = menu_guy.get_rect()
# menu_guy_rect.centerx = 250
# menu_guy_rect.centery = 250
#
# monetka = pygame.image.load('pic/monetka.png')
# monetka_rect = monetka.get_rect()
# monetka_rect.centerx = 460
# monetka_rect.centery = 30
#
# dereviya = pygame.image.load('pic/dereviya.png')
# dereviya_rect = dereviya.get_rect()
# dereviya_rect.centerx = 250
# dereviya_rect.centery = 250
#
# fonager2 = pygame.image.load('pic/fonager2.png')
# fonager2_rect = fonager2.get_rect()
# fonager2_rect.centerx = 250
# fonager2_rect.centery = 250
#
# bro = pygame.image.load('pic/bro.png')
# bro_rect = bro.get_rect()
# bro_rect.centerx = 250
# bro_rect.centery = 200
# bro_shift_speed = False
# bro_mode = 2
#
# phantom = pygame.image.load("pic/booooo.png")
#
#
# fon_igri = 2
# setings_mojno = False
# setings_active_button = False
# creators_mojno = False
# nazad_active_button = False
# exit_menu_active_button = False
# menu_active_button = False
# creators_active_button = False
# continu_mojno = False
# bro_speed = 1
# right_fon = False
# down_fon = False
# left_fon = False
# center_fon = False
# run = True
# m_of = False
# show_text = True
# screen = pygame.display.set_mode([WIDTH, HEIGHT])
# K_right = False
# K_left = False
# K_down = False
# K_up = False
# while run:
#     keys = pygame.key.get_pressed()
#     mouse_pos = pygame.mouse.get_pos()
#     screen.blit(fonager2, fonager2_rect)
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if m_of == False:
#                 fantom_mojno = True
#             if setings_mojno == True:
#                 if setings_rect.collidepoint(mouse_pos):
#                     setings_active_button = True
#
#             if nazad_rect.collidepoint(mouse_pos):
#                 creators_active_button = False
#                 setings_active_button = False
#             if continu_mojno == True:
#                 if continu_rect.collidepoint(mouse_pos):
#                     menu_active_button = False
#                     m_of = True
#             if exit_menu_active_button == True:
#                 if exit2_rect.collidepoint(mouse_pos):
#                     pygame == quit()
#                     run = False
#
#             if creators_mojno == True:
#                 if creators_rect.collidepoint(mouse_pos):
#                     creators_active_button = True
#
#             if nachalo_rect.collidepoint(mouse_pos):
#                 show_text = False
#                 m_of = True
#             if menu_rect.collidepoint(mouse_pos):
#                 menu_active_button = True
#             if exit_rect.collidepoint(mouse_pos):
#                 if show_text == True:
#                     pygame == quit()
#                     run = False
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONUP:
#             if m_of == False:
#                 fantom_mojno = False
#         if m_of == True:
#             if event.type == pygame.KEYUP:
#
#                 if event.key == pygame.K_RSHIFT:
#                     bro_shift_speed = False
#                 if event.key == pygame.K_UP:
#                     K_up = False
#                 if event.key == pygame.K_DOWN:
#                     K_down = False
#                 if event.key == pygame.K_RIGHT:
#                     K_right = False
#                 if event.key == pygame.K_LEFT:
#                     K_left = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     menu_active_button = True
#                 if event.key == pygame.K_RSHIFT:
#                     bro_shift_speed = True
#                 if event.key == pygame.K_KP_PLUS:
#                     speed = speed + 1
#                 if event.key == pygame.K_KP_MINUS:
#                     speed = speed - 1
#                 if event.key == pygame.K_RIGHT:
#                     K_right = True
#                 if event.key == pygame.K_LEFT:
#                     K_left = True
#                 if event.key == pygame.K_UP:
#                     K_up = True
#                 if event.key == pygame.K_DOWN:
#                     K_down = True
#     if K_right:
#         bro_mode = 2
#         bro_rect.x = bro_rect.x + bro_speed
#         bro2_rect.x = bro2_rect.x + bro_speed
#     if K_left:
#         bro_mode = 1
#         bro_rect.x = bro_rect.x - bro_speed
#         bro2_rect.x = bro2_rect.x - bro_speed
#     if K_up:
#         bro_rect.y = bro_rect.y - bro_speed
#         bro2_rect.y = bro2_rect.y - bro_speed
#     if K_down:
#         bro_rect.y = bro_rect.y + bro_speed
#         bro2_rect.y = bro2_rect.y + bro_speed
#
#     if m_of == True:
#         screen.blit(menu, menu_rect)
#         if  menu_rect.collidepoint(mouse_pos):
#             screen.blit(menu_active, menu_rect)
#         else:
#             screen.blit(menu, menu_rect)
#
#     if m_of == False:
#         if fantom_mojno == True:
#             screen.blit(phantom, mouse_pos)
#
#
#
#
#
#
#
#
#
#     """if bro_rect.y >= 290:
#         bro_rect.y = -290
#         bro2_rect.y = -290
#     if bro_rect.y <= -291:
#         bro_rect.y = 289
#         bro2_rect.y = 289
#     if bro_rect.x >= 290:
#         bro_rect.x = -290
#         bro2_rect.x = -290
#     if bro_rect.x <= -291:
#         bro_rect.x = 289
#         bro2_rect.x = 289"""
#
#     if m_of == True:
#         if keys[pygame.K_w]:
#             bro_rect.y = bro_rect.y - bro_speed
#             bro2_rect.y = bro2_rect.y - bro_speed
#         elif keys[pygame.K_a]:
#             bro_mode = 1
#             bro_rect.x = bro_rect.x - bro_speed
#             bro2_rect.x = bro2_rect.x - bro_speed
#         elif keys[pygame.K_s]:
#             bro_rect.y = bro_rect.y + bro_speed
#             bro2_rect.y = bro2_rect.y + bro_speed
#         elif keys[pygame.K_d]:
#             bro_mode = 2
#             bro_rect.x = bro_rect.x + bro_speed
#             bro2_rect.x = bro2_rect.x + bro_speed
#
#     if bro_shift_speed == True:
#         bro_speed = 2
#     elif bro_shift_speed == False:
#         bro_speed = 1
#     if bro_stamina <= 0:
#         bro_shift_speed == False
#
#     if show_text == True:
#         screen.blit(nazvanie, nazvanie_rect)
#         screen.blit(exit, exit_rect)
#         screen.blit(nachalo, nachalo_rect)
#         if  nachalo_rect.collidepoint(mouse_pos):
#             screen.blit(nachalo_active, nachalo_rect)
#         else:
#             screen.blit(nachalo, nachalo_rect)
#
#         if exit_rect.collidepoint(mouse_pos):
#             screen.blit(exit_active, exit_rect)
#         else:
#             screen.blit(exit, exit_rect)
#
#     if menu_active_button == False:
#         exit_menu_active_button = False
#         creators_mojno = False
#         setings_mojno = False
#         continu_mojno = False
#         setings_active_button = False
#         creators_active_button == False
#
#     if creators_active_button == False:
#         nazad_active_button == False
#     if bro_mode == 2:
#         screen.blit(bro, bro_rect)
#     if bro_mode == 1:
#         screen.blit(bro2, bro2_rect)
#     screen.blit(monetka, monetka_rect)
#     screen.blit(dereviya, dereviya_rect)
#
#     if menu_active_button == True:
#         exit_menu_active_button = True
#         creators_mojno = True
#         setings_mojno = True
#         continu_mojno = True
#         m_of = False
#         screen.blit(menu_guy, menu_guy_rect)
#         screen.blit(exit2, exit2_rect)
#         screen.blit(setings, setings_rect)
#         screen.blit(creators, creators_rect)
#         screen.blit(continu, continu_rect)
#         if exit2_rect.collidepoint(mouse_pos):
#             screen.blit(exit2_active, exit2_rect)
#         else:
#             screen.blit(exit2, exit2_rect)
#         if continu_rect.collidepoint(mouse_pos):
#             screen.blit(continu_active, continu_rect)
#         else:
#             screen.blit(continu, continu_rect)
#         if creators_rect.collidepoint(mouse_pos):
#             screen.blit(creators_active, creators_rect)
#         else:
#             screen.blit(creators, creators_rect)
#         if setings_rect.collidepoint(mouse_pos):
#             screen.blit(setings_active, setings_rect)
#         else:
#             screen.blit(setings, setings_rect)
#
#     if creators_active_button == True:
#         nazad_active_button = True
#         setings_mojno= False
#         exit_menu_active_button = False
#         continu_mojno = False
#         screen.blit(menu_guy, menu_guy_rect)
#         screen.blit(director, director_rect)
#         screen.blit(programist, programist_rect)
#         screen.blit(dizainer, dizainer_rect)
#         screen.blit(sponsor, sponsor_rect)
#         screen.blit(osobay_blagodarnost, osobay_blagodarnost_rect)
#         screen.blit(scenarist, scenarist_rect)
#         screen.blit(sozdately, sozdately_rect)
#         if nazad_active_button == True:
#             screen.blit(nazad, nazad_rect)
#             if nazad_rect.collidepoint(mouse_pos):
#                 screen.blit(nazad_active, nazad_rect)
#             else:
#                 screen.blit(nazad, nazad_rect)
#     if setings_active_button == True:
#         nazad_active_button = True
#         continu_mojno = False
#         screen.blit(menu_guy, menu_guy_rect)
#         if nazad_active_button == True:
#             screen.blit(nazad, nazad_rect)
#             if nazad_rect.collidepoint(mouse_pos):
#                 screen.blit(nazad_active, nazad_rect)
#             else:
#                 screen.blit(nazad, nazad_rect)
#         exit_menu_active_button = False
#         screen.blit(gromkost, gromkost_rect)
#         screen.blit(nastroiki, nastroiki_rect)
#     pygame.display.flip()
#     time.sleep(0.01)
# pygame.quit()
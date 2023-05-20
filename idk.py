import pygame
pygame.init()

WIDTH = 700
HEIGHT = 640

color_menu = [255, 0, 0]
color_menu_active = [0, 0, 255]

font_100 = pygame.font.Font(None, 100)  # None - шрифт, 100 - размер
font_50 = pygame.font.Font(None, 50)  # None - шрифт, 50 - размер
text = font_100.render("Название игры", True, [0, 0, 0])
text_rect = text.get_rect()
text_rect.center = WIDTH//2, HEIGHT//2 - 100
text_begin = font_50.render("Начать", True, color_menu)
text_begin_active = font_50.render("Начать", True, color_menu_active)
text_exit = font_50.render("Выйти", True, color_menu)
text_exit_active = font_50.render("Выйти", True, color_menu_active)
text_exit_rect = text_exit.get_rect()
text_exit_rect.center = WIDTH//2, HEIGHT//2 + 100
text_begin_rect = text_begin.get_rect()
text_begin_rect.center = WIDTH//2, HEIGHT//2
info_chet = font_50.render("Счёт: ", True, [0, 0, 0])
info_chet_rect = info_chet.get_rect()
info_chet_rect.topleft = 0, 0
info_menu = font_50.render("Меню", True, [0, 0, 0])
info_menu_rect = info_menu.get_rect()
info_menu_rect.topright = 0, 0
fon1r = font_50.render("Облака", True, [0, 0, 0])
fon1r_rect = fon1r.get_rect()
fon1r_rect.center = WIDTH//2, HEIGHT//2
fon2r = font_50.render("Столбы", True, [0, 0, 0])
fon2r_rect = fon2r.get_rect()
fon2r_rect.center = WIDTH//2, HEIGHT//2
fon3r = font_50.render("Лава", True, [0, 0, 0])
fon3r_rect = fon3r.get_rect()
fon3r_rect.center = WIDTH//2, HEIGHT//2
fon4r = font_50.render("Луг", True, [0, 0, 0])
fon4r_rect = fon4r.get_rect()
fon4r_rect.center = WIDTH//2, HEIGHT//2
import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

color_menu = [153,21,178]
color_menu_active = [181,164,38]

font_50 = pygame.font.Font('fonts/shrift_for_start.ttf', 50)
font_25 = pygame.font.Font('fonts/shrift_for_start.ttf', 25)
font_25 = pygame.font.Font('fonts/shrift_for_quest.ttf', 25)

nazvanie = font_50.render("Магия леса", True, color_menu)
nazvanie_rect = nazvanie.get_rect()
nazvanie_rect.center = WIDTH//2, HEIGHT//2 -200

nachalo = font_25.render("Начать", True, color_menu)
nachalo_active = font_25.render("Начать", True, color_menu_active)
nachalo_rect = nachalo.get_rect()
nachalo_rect.center = WIDTH//2, HEIGHT//2

exit = font_25.render("Выйти", True, color_menu)
exit_active = font_25.render("Выйти", True, color_menu_active)
exit_rect = exit.get_rect()
exit_rect.center = WIDTH//2, HEIGHT//2 + 50

menu = font_25.render("Меню", True, color_menu)
menu_active = font_25.render("Меню", True, color_menu_active)
menu_rect = menu.get_rect()
menu_rect.topleft = 0, 0

continu = font_50.render("Продолжить", True, color_menu)
continu_active = font_50.render("Продолжить", True, color_menu_active)
continu_rect = continu.get_rect()
continu_rect.center = WIDTH//2, HEIGHT//2 - 150

creators = font_50.render("Создатели", True, color_menu)
creators_active = font_50.render("Создатели", True, color_menu_active)
creators_rect = creators.get_rect()
creators_rect.center = WIDTH//2, HEIGHT//2 - 50

setings = font_50.render("Настройки", True, color_menu)
setings_active = font_50.render("Настройки", True, color_menu_active)
setings_rect = setings.get_rect()
setings_rect.center = WIDTH//2, HEIGHT//2 + 50

exit2 = font_50.render("Выход", True, color_menu)
exit2_active = font_50.render("Выход", True, color_menu_active)
exit2_rect = exit2.get_rect()
exit2_rect.center = WIDTH//2, HEIGHT//2 + 150

sozdately = font_50.render("Создатели:", True, color_menu)
sozdately_rect = sozdately.get_rect()
sozdately_rect.center = WIDTH//2, HEIGHT//2 - 150

director = font_25.render("Директор: DeWoolf", True, color_menu)
director_rect = director.get_rect()
director_rect.center = WIDTH//2, HEIGHT//2 - 100

programist = font_25.render("Программист: DeWoolf", True, color_menu)
programist_rect = programist.get_rect()
programist_rect.center = WIDTH//2, HEIGHT//2 - 50

scenarist = font_25.render("Сценарист: DeWoolf", True, color_menu)
scenarist_rect = scenarist.get_rect()
scenarist_rect.center = WIDTH//2, HEIGHT//2

dizainer = font_25.render("Дизайнер: DeWoolf", True, color_menu)
dizainer_rect = dizainer.get_rect()
dizainer_rect.center = WIDTH//2, HEIGHT//2 + 50

sponsor = font_25.render("Спонсор: DeWoolf", True, color_menu)
sponsor_rect = sponsor.get_rect()
sponsor_rect.center = WIDTH//2, HEIGHT//2 + 100

osobay_blagodarnost = font_25.render("Особая благодарность: DeWoolf", True, color_menu)
osobay_blagodarnost_rect = osobay_blagodarnost.get_rect()
osobay_blagodarnost_rect.center = WIDTH//2, HEIGHT//2 + 150

nazad = font_50.render("Назад", True, color_menu)
nazad_active = font_50.render("Назад", True, color_menu_active)
nazad_rect = nazad.get_rect()
nazad_rect.center = WIDTH//2, HEIGHT//2 + 190

gromkost = font_25.render("Громкость", True, color_menu)
gromkost_rect = gromkost.get_rect()
gromkost_rect.center = WIDTH//2 - 100, HEIGHT//2 - 100

nastroiki = font_50.render("Настройки", True, color_menu)
nastroiki_rect = nastroiki.get_rect()
nastroiki_rect.center = WIDTH//2, HEIGHT//2 - 190

pobeda = font_50.render('Ты выиграл!!!', True, [255, 0, 0])
pobeda_rect = pobeda.get_rect()
pobeda_rect.center = WIDTH//2, HEIGHT//2

zanovo = font_25.render("Заново", True, color_menu)
zanovo_active = font_25.render("Заново", True, color_menu_active)
zanovo_rect = zanovo.get_rect()
zanovo_rect.center = WIDTH//2, HEIGHT//2 + 50

exit3 = font_25.render("Выйти", True, color_menu)
exit3_active = font_25.render("Выйти", True, color_menu_active)
exit3_rect = exit3.get_rect()
exit3_rect.center = WIDTH//2, HEIGHT//2 + 100
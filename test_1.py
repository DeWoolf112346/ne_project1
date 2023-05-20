import pygame

pygame.init()

pygame.mixer.music.load("music/pobeda_music.mp3")
pygame.mixer.music.play()

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)
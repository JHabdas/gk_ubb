import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zad. 2")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)

win.fill(BIALY)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Rysowanie prostokata za pomoca kwadratow
    pygame.draw.rect(win, NIEBIESKI, (160, 250, 80, 80))
    pygame.draw.rect(win, NIEBIESKI, (240, 250, 80, 80))
    pygame.draw.rect(win, NIEBIESKI, (320, 250, 80, 80))

    #Rysowanie trojkatow
    pygame.draw.polygon(win, NIEBIESKI, ([280, 250], [340, 180], [220, 180]))
    pygame.draw.polygon(win, NIEBIESKI, ([280, 330], [340, 400], [220, 400]))

    pygame.display.update()
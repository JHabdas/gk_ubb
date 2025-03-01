import pygame
import math

pygame.init()

width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zad. 1")

# Stałe
center = (width // 2, height // 2)
radius = 150
sides = 7
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Funkcja generująca punkty
def generate_points(angle=0, x_shift=0, y_shift=0, x_scale=1, y_scale=1, skew=0, tilt_up=False):
    return [
        (
            center[0] + x_shift + x_scale * radius * math.cos(2 * math.pi * i / sides + math.radians(angle)) + skew * math.sin(2 * math.pi * i / sides),
            center[1] + y_shift + y_scale * radius * math.sin(2 * math.pi * i / sides + math.radians(angle)) - (20 * math.sin(2 * math.pi * i / sides) if tilt_up else 0)
        )
        for i in range(sides)
    ]

# Początkowy rysunek
win.fill(YELLOW)
pygame.draw.polygon(win, BLUE, generate_points())
pygame.display.flip()

# Główna pętla
running = True
while running:
    keys = pygame.key.get_pressed()
    
    transformations = {
        pygame.K_1: generate_points(),
        pygame.K_2: generate_points(angle=45),
        pygame.K_3: generate_points(angle=180, x_scale=0.5),
        pygame.K_4: generate_points(skew=20),
        pygame.K_5: generate_points(y_shift=-200, y_scale=0.3),
        pygame.K_6: generate_points(angle=90, tilt_up=True),
        pygame.K_7: generate_points(angle=180, x_scale=-1, y_scale=1.5),
        pygame.K_8: generate_points(angle=225, x_shift=-100, y_shift=100),
        pygame.K_9: generate_points(angle=180, x_shift=100, x_scale=-1)
    }
    
    for key, points in transformations.items():
        if keys[key]:
            win.fill(YELLOW)
            pygame.draw.polygon(win, BLUE, points)
            pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
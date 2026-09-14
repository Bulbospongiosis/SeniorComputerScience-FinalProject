import pygame
import sys
import math

pygame.init()

WIDTH,HEIGHT = 1250,750

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Trebuchet Simulation")
clock = pygame.time.Clock()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
GREEN = (50,200,50)
RED = (255,0,0)
PURPLE = (128,0,128)
ORANGE = (255, 165, 0)

#Variables
FrameRate = 24

#Defs
def Draw():
    screen.fill(WHITE)


Draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    Draw()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
sys.exit()
import pygame
import os

#variables
NextAvailableUnit = 0
NextAvailableEnemy = 0

#images


def Button(screen,UnitButton):
    screen.blit(pygame.transform.scale(UnitButton, (100, 108)),(100,100))



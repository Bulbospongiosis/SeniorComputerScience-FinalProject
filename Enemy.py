import pygame

WIDTH,HEIGHT = 1250,750

class Enemy:
    def __init__(self):
        self.EnemyX = WIDTH
        self.EnemyType = 0
        self.EnemyAnimation = 0
        self.EnemyAtkAnimation = 0
        self.EnemyCooldown = 0
        self.EnemyHealth = 0
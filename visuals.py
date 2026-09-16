import pygame

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
GREEN = (50,200,50)
RED = (255,0,0)
PURPLE = (128,0,128)
ORANGE = (255, 165, 0)

WIDTH,HEIGHT = 1250,750

def Draw(screen,data,UnitX,UnitType,UnitAnimation,EnemyX,UnitY,EnemyY,EnemyType,UnitCount,EnemyCount):
    screen.fill(WHITE)
    #pygame.draw.rect(screen,BLACK,(0,0,100,100))
    
    for i in range(UnitCount):
        if UnitX[i] > 0:
            
            pygame.draw.rect(screen,BLACK,(UnitX[i] - data["Units"][UnitType[i]]["UnitSize"],UnitY - (2 * data["Units"][UnitType[i]]["UnitSize"]),data["Units"][UnitType[i]]["UnitSize"],2 * data["Units"][UnitType[i]]["UnitSize"]))
    for i in range(EnemyCount):
        if EnemyX[i] < WIDTH:
            
            pygame.draw.rect(screen,BLACK,(EnemyX[i],EnemyY - data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"]))


def DrawButtons(screen,UnitButton,UnitButtonSetup,ButtonError,Cooldown,data,FrameRate,AssignedButtonTypes):
    for i in range(5):
        if ButtonError[i] == False:
            screen.blit(UnitButtonSetup[i], (125 + (200 * i),50))
        else:
            screen.blit(tint_image_red(UnitButtonSetup[i],0.6), (125 + (200 * i),50))

        if ButtonError[i+5] == False:
            screen.blit(UnitButtonSetup[i+5], (125 + (200 * i),175))
        else:
            screen.blit(tint_image_red(UnitButtonSetup[i+5],0.6), (125 + (200 * i),175))
        if Cooldown[i] < data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate:
            full_overlay = pygame.Surface((200, 125), pygame.SRCALPHA)
            full_overlay.fill((0, 0, 0, 100))  # Adjust alpha (e.g., 100) for desired transparency
            screen.blit(full_overlay, (125 + (200 * i), 50))

            width = int(200 * Cooldown[i] / (data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate))
            cooldown_surface = pygame.Surface((width, 125), pygame.SRCALPHA)
            cooldown_surface.fill((0, 0, 0, 128))  # Semi-transparent black
            screen.blit(cooldown_surface, (125 + (200 * i), 50))

        # For the second button group (i+5)
        if Cooldown[i+5] < data["Units"][AssignedButtonTypes[i+5]]["UnitCooldown"] * FrameRate:
            full_overlay = pygame.Surface((200, 125), pygame.SRCALPHA)
            full_overlay.fill((0, 0, 0, 100))  
            screen.blit(full_overlay, (125 + (200 * i), 175))

            width = int(200 * Cooldown[i+5] / (data["Units"][AssignedButtonTypes[i+5]]["UnitCooldown"] * FrameRate))
            cooldown_surface = pygame.Surface((width, 125), pygame.SRCALPHA)
            cooldown_surface.fill((0, 0, 0, 128))  # Semi-transparent black
            screen.blit(cooldown_surface, (125 + (200 * i), 175))
def tint_image_red(image_surface, tint_intensity):

    tinted = image_surface.copy()
    
    r = 255
    g = int(255 * (1 - tint_intensity))
    b = int(255 * (1 - tint_intensity))
    
    tinted.fill((r, g, b, 255), special_flags=pygame.BLEND_RGBA_MULT)
    
    return tinted
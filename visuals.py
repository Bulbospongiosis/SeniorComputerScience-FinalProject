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


def DrawButtons(screen,UnitButton,UnitButtonSetup,ButtonError,Cooldown,data,FrameRate,AssignedButtonTypes,JewButtonError,JewButtonSetup):
    pygame.draw.rect(screen,BLACK,(90,515,770,220))
    for i in range(5):
        if ButtonError[i] == False:
            screen.blit(UnitButtonSetup[AssignedButtonTypes[i]], (100 + (150 * i),500 + 25))
        else:
            screen.blit(tint_image_red(UnitButtonSetup[AssignedButtonTypes[i]],0.6), (100 + (150 * i),500 + 25))

        if ButtonError[i+5] == False:
            screen.blit(UnitButtonSetup[AssignedButtonTypes[i+5]], (100 + (150 * i),600 + 25))
        else:
            screen.blit(tint_image_red(UnitButtonSetup[AssignedButtonTypes[i+5]],0.6), (100 + (150 * i),600 + 25))
        if Cooldown[i] < data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate:
            full_overlay = pygame.Surface((150, 100), pygame.SRCALPHA)
            full_overlay.fill((0, 0, 0, 100))  # Adjust alpha (e.g., 100) for desired transparency
            screen.blit(full_overlay, (100 + (150 * i), 500 + 25))

            width = int(150 * Cooldown[i] / (data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate))
            cooldown_surface = pygame.Surface((width, 100), pygame.SRCALPHA)
            cooldown_surface.fill((0, 0, 0, 128))  # Semi-transparent black
            screen.blit(cooldown_surface, (100 + (150 * i), 500 + 25))

        # For the second button group (i+5)
        if Cooldown[i+5] < data["Units"][AssignedButtonTypes[i+5]]["UnitCooldown"] * FrameRate:
            full_overlay = pygame.Surface((150, 100), pygame.SRCALPHA)
            full_overlay.fill((0, 0, 0, 100))  
            screen.blit(full_overlay, (100 + (150 * i), 600 + 25))

            width = int(150 * Cooldown[i+5] / (data["Units"][AssignedButtonTypes[i+5]]["UnitCooldown"] * FrameRate))
            cooldown_surface = pygame.Surface((width, 100), pygame.SRCALPHA)
            cooldown_surface.fill((0, 0, 0, 128))  # Semi-transparent black
            screen.blit(cooldown_surface, (100 + (150 * i), 600 + 25))
    if JewButtonError == False:
        screen.blit(JewButtonSetup, (900,500))
    else:
        screen.blit(tint_image_red(JewButtonSetup,0.6), (900,500))
def tint_image_red(image_surface, tint_intensity):

    tinted = image_surface.copy()
    
    r = 255
    g = int(255 * (1 - tint_intensity))
    b = int(255 * (1 - tint_intensity))
    
    tinted.fill((r, g, b, 255), special_flags=pygame.BLEND_RGBA_MULT)
    
    return tinted

def textplacement(screen,data,Money,MoneyLimit,JewButtonLevel):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    MidText = pygame.font.Font('freesansbold.ttf',30)
    MidText2 = pygame.font.Font('freesansbold.ttf',36)
    TextSurf, TextRect = text_objects(str(int(Money)) + "¢/" + str(int(MoneyLimit)) + "¢", largeText)
    TextRect.center = (WIDTH - 210,60)
    
    screen.blit(TextSurf,TextRect)
    
    screen.blit(render_thick_outlined_text((str(int(MoneyLimit - 1500)) + "¢" ), MidText, BLACK,WHITE,2),(976,685))
    screen.blit(render_thick_outlined_text("LeveL " + str(int(JewButtonLevel)), MidText2, BLACK,WHITE,3),(955,510))
    

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def render_thick_outlined_text(text, font, text_color, outline_color, thickness):
    text_surface = font.render(text, True, text_color)
    
    # Get the outline shape from the rendered text mask
    mask = pygame.mask.from_surface(text_surface)
    outline_surface = mask.to_surface(setcolor=outline_color, unsetcolor=(0,0,0,0))
    
    # Create output surface with padding for thickness
    w, h = text_surface.get_size()
    combined = pygame.Surface((w + 2 * thickness, h + 2 * thickness), pygame.SRCALPHA)
    
    # Draw outline shifted in all directions
    for dx in range(-thickness, thickness + 1):
        for dy in range(-thickness, thickness + 1):
            if dx*dx + dy*dy <= thickness*thickness: # Keep outline circular
                combined.blit(outline_surface, (dx + thickness, dy + thickness))
                
    # Place original text in center
    combined.blit(text_surface, (thickness, thickness))
    return combined
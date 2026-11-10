import pygame

pygame.font.init()

WHITE = (255,255,255)
BLUE = (50,150,255)

TITLE_FONT = pygame.font.Font("Fonts/ScratchKidsRegular-2vn5w.ttf", 175)
HEADING_FONT = pygame.font.Font("Fonts/MinecraftTen-VGORe.ttf", 35)


def menuappear(AssignedButtonTypes,data,screen,background,UnitButtonSetup,input_index,displayUnit):
    # Draw original background
    screen.blit(background, (0, 0))

    WIDTH, HEIGHT = screen.get_size()

    # Game title
    title = TITLE_FONT.render("BATTLE KATS", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 105)))

    # Title underline
    #pygame.draw.line(screen, BLUE, (400, 110), (850, 110), 3)

    # Character selection heading
    heading = HEADING_FONT.render("CHOOSE YOUR TEAM", True, WHITE)
    screen.blit(heading, heading.get_rect(center=(480, 475)))

    # Character selection border
    pygame.draw.rect(screen, BLUE, (85, 510, 780, 232), 2)

    screen.blit(displayUnit, ((WIDTH/2)-150,200))

    pygame.draw.polygon(screen,WHITE,(((WIDTH/2)-250,200),((WIDTH/2)-250,400),((WIDTH/2)-400,300)))
    pygame.draw.polygon(screen,WHITE,(((WIDTH/2)+250,200),((WIDTH/2)+250,400),((WIDTH/2)+400,300)))

def ShiftInputLeft(input_index):
    
    return input_index

def ShiftInputRight(input_index):
    if input_index > 0:
        input_index += 1
    return input_index

def ApplyInput(next,AssignedButtonTypes,input_index):
    if next < 10:
        AssignedButtonTypes[next] = input_index
        next += 1
    return next
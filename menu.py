import pygame

pygame.font.init()

WHITE = (255,255,255)
BLUE = (50,150,255)

TITLE_FONT = pygame.font.SysFont("arial", 52, bold=True)
HEADING_FONT = pygame.font.SysFont("arial", 25, bold=True)


def menuappear(AssignedButtonTypes,data,screen,background,UnitButtonSetup,input_index):
    # Draw original background
    screen.blit(background, (0, 0))

    WIDTH, HEIGHT = screen.get_size()

    # Game title
    title = TITLE_FONT.render("BATTLE KATS", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 65)))

    # Title underline
    pygame.draw.line(screen, BLUE, (400, 110), (850, 110), 3)

    # Character selection heading
    heading = HEADING_FONT.render("CHOOSE YOUR TEAM", True, WHITE)
    screen.blit(heading, heading.get_rect(center=(478, 470)))

    # Character selection border
    pygame.draw.rect(screen, BLUE, (85, 510, 780, 232), 2)

    screen.blit(pygame.transform.scale(UnitButtonSetup[input_index],(300,200)), ((WIDTH/2)-150,200))

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
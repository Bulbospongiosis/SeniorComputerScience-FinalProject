import pygame

pygame.font.init()

WHITE = (255,255,255)
BLUE = (50,150,255)

TITLE_FONT = pygame.font.SysFont("arial", 52, bold=True)
HEADING_FONT = pygame.font.SysFont("arial", 25, bold=True)


def menuappear(AssignedButtonTypes, data, screen, background):

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
    screen.blit(heading, heading.get_rect(center=(500, 465)))

    # Character selection border
    pygame.draw.rect(screen, BLUE, (85, 510, 780, 232), 2)
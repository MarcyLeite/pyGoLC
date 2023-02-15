def generate(pygame, screen, board_size, panel_size, font):
    pygame.draw.rect(screen, (20, 20, 70), pygame.Rect(board_size, 0, panel_size, board_size))
    img = font.render('Space - start / pause', True, (255, 255, 255))
    screen.blit(img, (board_size + 20, 70))
    img = font.render('Delete - Clear Board', True, (255, 255, 255))
    screen.blit(img, (board_size + 20, 100))
    img = font.render('G - GGG Preset', True, (255, 255, 255))
    screen.blit(img, (board_size + 20, 130))

def running_status(pygame, screen, board_size, running):
    color = (128, 255, 128)
    if not running:
        color = (255, 128, 128)
    pygame.draw.rect(screen, color, pygame.Rect(board_size + 20, 30, 20, 20))
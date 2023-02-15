import panel
import mouse_handler
import board
import golc
import pygame
import load_preset

cell_size = 10
board_size = 600
panel_size = 200

def main():
    
    # Setup
    pygame.init()
    pygame.display.set_caption("Comway's Game of Life")

    screen = pygame.display.set_mode((board_size + panel_size, board_size))
    font = pygame.font.SysFont(None, 24)

    new_board = board.generate(pygame, screen, board_size, cell_size)
    panel.generate(pygame, screen, board_size, panel_size, font)
    
    clock = pygame.time.Clock()

    running = False
    
    # Main Loop

    while True:
        mouse_click = 0

        # Get Events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.button
            if event.type == pygame.KEYDOWN:
                if(event.unicode == ' '):
                    running = not running
                if(event.unicode == 'g'):
                    new_board = load_preset.gosper_glider_gun(new_board)
                if(event.unicode == '\x7f'):
                    new_board = load_preset.clear(new_board)
        mouse_pos = pygame.mouse.get_pos()
        
        # DO
        if not running:
            mouse_handler.board_behavior(pygame, screen, new_board, mouse_pos, mouse_click, cell_size)
        else:
            clock.tick(10)
            new_board = golc.apply_rules(new_board)
        board.render(pygame, screen, new_board, cell_size)
        panel.running_status(pygame, screen, board_size, running)
        pygame.display.update()

if __name__ == "__main__":
    main()
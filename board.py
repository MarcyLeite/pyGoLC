import load_preset

def generate(pygame, screen, board_size, cell_size):
    board = [[{ 'active': False, 'hover': False } for column in range(int(board_size/cell_size))] for line in range(int(board_size/cell_size))]
    return board

def render(pygame, screen, board, cell_size):
    x = 0
    for line in board:
        y = 0
        for cell in line:
            if not cell['active']:
                color = (0, 0, 0)
                if cell['hover']:
                    color = (128, 128, 128)
            else:
                color = (255, 255, 255)
                if cell['hover']:
                    color = (255, 128, 128)
            pygame.draw.rect(screen, color, pygame.Rect(x,y, cell_size, cell_size))
            cell['hover'] = False
            y += cell_size
        x += cell_size
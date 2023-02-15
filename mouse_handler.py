def board_behavior(pygame, screen, board, mouse_pos, mouse_click, cell_size):
    if mouse_pos[0] >= 600:
        return
    relative_x = int(mouse_pos[0]/cell_size)
    relative_y = int(mouse_pos[1]/cell_size)
    board[relative_x][relative_y]['hover'] = True
    if mouse_click == 1:
        board[relative_x][relative_y]['active'] = True
    if mouse_click == 3:
        board[relative_x][relative_y]['active'] = False


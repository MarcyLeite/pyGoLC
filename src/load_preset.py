def clear(board):
    for x in enumerate(board):
        for y in enumerate(board):
            board[x[0]][y[0]]['active'] = False
    return board

def gosper_glider_gun(board):
    
    board = clear(board)

    # Left Bouncer
    board[11][11]['active'] = True
    board[11][12]['active'] = True
    board[12][11]['active'] = True
    board[12][12]['active'] = True

    # Left Generator
    board[21][11]['active'] = True
    board[21][12]['active'] = True
    board[21][13]['active'] = True
    board[22][14]['active'] = True
    board[23][15]['active'] = True
    board[24][15]['active'] = True
    board[22][10]['active'] = True
    board[23][9]['active'] = True
    board[24][9]['active'] = True
    board[25][12]['active'] = True
    board[26][14]['active'] = True
    board[27][13]['active'] = True
    board[27][12]['active'] = True
    board[27][11]['active'] = True
    board[28][12]['active'] = True
    board[26][10]['active'] = True

    # Right Generator
    board[31][11]['active'] = True
    board[31][10]['active'] = True
    board[31][9]['active'] = True
    board[32][11]['active'] = True
    board[32][10]['active'] = True
    board[32][9]['active'] = True
    board[33][8]['active'] = True
    board[33][12]['active'] = True
    board[35][12]['active'] = True
    board[35][13]['active'] = True
    board[35][8]['active'] = True
    board[35][7]['active'] = True

    #Right Bloucer
    board[45][9]['active'] = True
    board[45][10]['active'] = True
    board[46][9]['active'] = True
    board[46][10]['active'] = True
    
    return board
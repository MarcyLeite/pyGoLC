def apply_rules(board):
    new_board = []
    for lineTuple in enumerate(board):
        x = lineTuple[0]
        line = lineTuple[1]
        new_board.append([])
        for columnTuple in enumerate(line):
            y = columnTuple[0]
            cell = columnTuple[1]

            neighbours = 0

            for i in range(3):
                nx = x-1 + i
                for j in range(3):
                    ny = y-1 + j
                    if nx == x and ny == y:
                        continue
                    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
                        continue
                    if board[nx][ny]['active']:
                        neighbours += 1

            if cell['active']:
                if neighbours < 2 or neighbours > 3:
                    new_board[x].append({'active': False, 'hover': False})
                else:
                    new_board[x].append({'active': True, 'hover': False})
            else:
                if neighbours == 3:
                    new_board[x].append({'active': True, 'hover': False})
                else:
                    new_board[x].append({'active': False, 'hover': False})
    return new_board
    
    

            
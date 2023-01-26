
board = [[' ' for x in range(3)] for y in range(3)]


def check_win(player):
    
    for row in board:
        if row == [player, player, player]:
            return True
    
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def check_draw():
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True


player = 'X'
while True:
    
    for row in board:
        print(row)
    
    x, y = input("Player " + player + ", choose your position (x y): ").split()
    x, y = int(x), int(y)
    
    if board[x][y] == ' ':
        board[x][y] = player
    else:
        print("This position is already taken!")
        continue
    
    if check_win(player):
        print("Player " + player + " wins!")
        break
    if check_draw():
        print("It's a draw!")
        break
    
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

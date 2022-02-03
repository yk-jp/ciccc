import random


def define_symbols() -> (str, str):
    symbols = ["X", "O"]
    random.shuffle(symbols)

    print("Tic-Tac-Toe!")
    print(f"Player is {symbols[0]} and Computer is {symbols[1]}")

    return symbols[0], symbols[1]


def define_movement(player_choice: int, board: [[int]], pattern: [[int]]) -> int:
    temp_list = []

    for idx in pattern:
        if player_choice in idx:
            idx.remove(player_choice)
            temp_list.append(idx)

    x = random.randint(0, len(temp_list) - 1)
    y = random.randint(0, len(idx) - 1)

    best_position = temp_list[x][y]
    return best_position


def print_board(board):
    print()
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print()


def select_space(board, move, turn):
    if move not in range(1, 10):
        return False
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        print("Invalid move! Please try again!")
        return False


def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves


def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

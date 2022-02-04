import random

patterns = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def define_symbols() -> (str, str):
    """
    This function define which symbol will be used by player and computer
    :return: (str, str)
    """
    symbols = ["X", "O"]
    random.shuffle(symbols)
    print("Tic-Tac-Toe!")
    print(f"Player is {symbols[0]} and Computer is {symbols[1]}")
    return symbols[0], symbols[1]


def print_board(board: [[int]]) -> None:
    """
    This function prompt board to player
    :param board: Game board
    :return: None
    """
    print()
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print()


def get_best_position_win(_, board, computer_symbol) -> (bool, [int]):
    """
    This function returns the best movement to computer win
    :param _: (Not used) possible movements
    :param board: Game board
    :param computer_symbol: symbol that identify computer
    :return: (bool, [int]) bool is used to an attack movement and best possible movement
    """
    can_win = False
    best_win_position = None

    for idx in patterns:
        occurrences = 0
        for jdx in idx:
            row = int((jdx - 1) / 3)
            col = (jdx - 1) % 3

            if board[row][col] == computer_symbol:
                occurrences += 1

        if occurrences == 2:
            can_win = True
            best_win_position = idx
            return can_win, best_win_position
    return can_win, best_win_position


def define_movement(player_choice: int, board: [[int]], computer_symbol: str, target_list: []) -> int:
    """
    This function define which board's position should computer choose
    :param computer_symbol: Symbol that represents a computer in board
    :param player_choice: Last player movement
    :param board: Game board
    :return: Best position to computer move
    """
    temp_list = []
    best_position = None

    for idx in patterns:
        if player_choice in idx:
            if len(idx) == 0:
                temp_list = temp_list.remove(idx)

            idx.remove(player_choice)

            for jdx in target_list:
                if jdx in idx:
                    idx.remove(jdx)

            temp_list.append(idx)

    possible_win, best_win_position = get_best_position_win(temp_list, board, computer_symbol)

    if possible_win:
        for idx in best_win_position:
            if idx in available_moves(board):
                best_position = idx
    else:
        random_vertical = random.randint(0, len(temp_list) - 1)
        random_horizontal = 0

        if random_horizontal not in available_moves(board):
            best_position = temp_list[random_vertical][random_horizontal]
        else:
            random_horizontal = 1
            best_position = temp_list[random_vertical][random_horizontal]

    return best_position


def select_space(board: [[int]], move: int, turn) -> bool:
    """
    This function marks a position in board to player or computer
    :param board: Game board
    :param move: Position to be marked
    :param turn: Who is requesting
    :return: Return false case a position cannot be marked or if invalid. Return true if marked
    """
    if move is not None:
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        if board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = turn
            return True
    print("Invalid move! Please try again!")
    return False


def available_moves(board: [[int]]) -> [int]:
    """
    This function returns all available movements that a player can use
    :param board: Game board
    :return: List with all available positions
    """
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves


def has_won(board: [[int]], player: str) -> bool:
    """
    This function checks if a player has won
    :param board: Game board
    :param player: Who is requesting - player or computer
    :return: Returns false case not and true case yes
    """
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

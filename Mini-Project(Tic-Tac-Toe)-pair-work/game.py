from tic_tac_toe import *

has_winner = False
player_symbol, computer_symbol = define_symbols()


my_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

target_list = []

while not has_winner:

    if len(available_moves(my_board)) == 0:
        print_board(my_board)
        print("It's a draw!")
        has_winner = True
        break

    print_board(my_board)
    player_choice = input("Please make your move! [1-9]: ")

    if not player_choice.isdigit() or int(player_choice) < 1 or int(player_choice) > 9:
        print("Invalid input! Please enter a number!")
        continue

    select_space(my_board, int(player_choice), player_symbol)

    if has_won(my_board, player_symbol):
        print_board(my_board)
        print("Congratulations! You won!")
        has_winner = True
        break

    best_position = define_movement(int(player_choice), my_board, computer_symbol, target_list)
    target_list.append(best_position)
    select_space(my_board, best_position, computer_symbol)

    if has_won(my_board, computer_symbol):
        print_board(my_board)
        print("Sorry, Computer won!")
        has_winner = True
        break

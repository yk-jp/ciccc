# helper
from helper.is_current_player_winner import is_current_player_winner
from helper.player_select_mark import player_select_mark
from helper.draw_result import draw_result
from helper.update_game_board import update_game_board
from helper.is_draw import is_draw
from helper.display_results import display_results 

# config
from config.config import player_input_constraint
from config.config import square_area

def main():
    #default settings
    player_mark_list = [" "] * square_area #str type
    players = ['0','X']

    # start the game
    print('Tic-Tac-Toe!')
    print('Player1 is 0 and Player2 is X.')

    game_round = len(player_mark_list)
    round_count = 0
    is_winner_decided = False
    
    while round_count < game_round:
        draw_result(player_mark_list)
        # player input
        curr_player = players[round_count%2]
        player_mark_at = player_select_mark(curr_player,player_mark_list)

        if player_mark_at == -1:
           # iterate player_select_mark until player selects a valid number 
           continue

        # mark on the game board
        player_mark_list = update_game_board(player_mark_list,curr_player,player_mark_at-1)

        if round_count > 2: 
            is_winner_decided = is_current_player_winner(player_mark_list,curr_player,player_mark_at-1)

            if is_winner_decided: 
                display_results(player_mark_list,curr_player,player_mark_at-1, round_count,is_winner_decided)
                break
        
        # count up round_count
        round_count+=1
    
    if not is_winner_decided and is_draw(round_count,game_round):
        display_results(player_mark_list,curr_player,player_mark_at-1, round_count,is_winner_decided)
    
if __name__ == '__main__':
    main()

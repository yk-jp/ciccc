from .is_draw import is_draw
from .draw_result import draw_result

def display_results(player_mark_list,player,player_mark_at,round_count,isWinner=False):
    if isWinner:
        draw_result(player_mark_list)
        print(f'Congratulations! {player} You won!')
        return 
    elif is_draw(round_count,len(player_mark_list)): #draw
        print('It\'s a draw!')
        return
    # still in progress
    return 

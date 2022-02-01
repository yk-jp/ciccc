from config.config import winning_pattern 

def is_current_player_winner(player_mark_list,player_mark,player_mark_at):
    # check all winning pattern that contain the last player_mark_at
    for i in range(len(winning_pattern)):
        curr_pattern = winning_pattern[i]

        if player_mark_at not in curr_pattern:
            continue

        # check a pattern
        if player_mark_list[curr_pattern[0]] == player_mark and player_mark_list[curr_pattern[1]] == player_mark and player_mark_list[curr_pattern[2]] == player_mark:
            return True

    return False
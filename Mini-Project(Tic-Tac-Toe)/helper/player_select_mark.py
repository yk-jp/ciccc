def player_select_mark(curr_player, player_mark_list):
    player_input = -1
    try:
        # type check
        player_input = int(input(f"[{curr_player}] Please make your move! {player_input_constraint['lowest']}-{player_input_constraint['highest']}:"))
        # whether the input number is not out of range
        if not (player_input_constraint["lowest"] <= player_input <= player_input_constraint["highest"]):
            raise Exception
    except Exception:
        print('Invalid Input! Please enter a number!')
        return -1

    try:
        if player_mark_list[player_input-1] != ' ':
            raise Exception
    except Exception:
        print('The position is already taken.')
        return -1

    return player_input
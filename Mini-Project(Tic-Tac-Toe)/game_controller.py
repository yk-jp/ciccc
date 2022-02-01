from config import player_input_constraint,winning_pattern


def player_select_mark(curr_player, player_mark_list):
    player_input = -1
    try:
        # type check
        player_input = int(input(
            f"[{curr_player}] Please make your move! {player_input_constraint['lowest']}-{player_input_constraint['highest']}:"))
        # whether the input number is not out of range
        if not (player_input_constraint["lowest"] <= player_input <= player_input_constraint["highest"]):
            raise Exception
    except Exception:
        print('Invalid Input! Please enter a number!')
        return -1

    try:
        if player_mark_list[player_input - 1] != ' ':
            raise Exception
    except Exception:
        print('The position is already taken.')
        return -1

    return player_input


def is_draw(round_count, round_total):
    return round_count >= round_total


def update_game_board(player_mark_list, player, mark_at):
    player_mark_list[mark_at] = player

    return player_mark_list


def draw_result(player_mark_list):
    for i in range(len(player_mark_list)):
        # ajust space
        if i % 3 == 0:
            print('  ', end='')

        # get data from ele
        ele = str(player_mark_list[i])
        # draw a mark
        print(ele, end=' ')

        # adjust layout
        if i % 3 != 2:
            print('|', end=' ')
        # create border
        if i % 3 == 2 and i != len(player_mark_list) - 1:
            print('')
            print('', '---|---|---')

    # line break
    print('')


def display_results(player_mark_list, player, player_mark_at, round_count, isWinner=False):
    if isWinner:
        draw_result(player_mark_list)
        print(f'Congratulations! {player} You won!')
        return
    elif is_draw(round_count, len(player_mark_list)):  # draw
        print('It\'s a draw!')
        return
    # still in progress
    return


def is_current_player_winner(player_mark_list, player_mark, player_mark_at):
    # check all winning pattern that contain the last player_mark_at
    for i in range(len(winning_pattern)):
        curr_pattern = winning_pattern[i]

        if player_mark_at not in curr_pattern:
            continue

        # check a pattern
        if player_mark_list[curr_pattern[0]] == player_mark and player_mark_list[curr_pattern[1]] == player_mark and \
                player_mark_list[curr_pattern[2]] == player_mark:
            return True

    return False

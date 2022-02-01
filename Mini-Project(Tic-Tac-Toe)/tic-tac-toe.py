player_input_constraint = {
    "lowest": 1,
    "highest": 9
}

winning_pattern = [ 
  [0,1,2],
  [0,3,6],
  [0,4,8],
  [1,4,7],
  [2,4,6],
  [2,5,8],
  [3,4,5],
  [6,7,8]
]

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

def draw_result(player_mark_list):
    for i in range(len(player_mark_list)):
        # ajust space
        if i%3 == 0:
            print('  ',end='')

        # get data from ele
        ele = str(player_mark_list[i])
        # draw a mark
        print(ele, end=' ')

        # adjust layout
        if i % 3 != 2:
            print('|',end=' ')
        # create border
        if i%3 == 2 and i != len(player_mark_list)-1:
            print('')
            print('','---|---|---')
    
    # line break
    print('')

def update_game_board(player_mark_list,player,mark_at):
    player_mark_list[mark_at] = player
    return player_mark_list 

def isDraw(round_count,round_total):
    return round_count >= round_total

def display_results(player_mark_list,player,player_mark_at,round_count,isWinner=False):
    if isWinner:
        draw_result(player_mark_list)
        print(f'Congratulations! {player} You won!')
        return 
    elif isDraw(round_count,len(player_mark_list)): #draw
        print('It\'s a draw!')
        return
    # still in progress
    return 

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

def main():
    #default settings
    edge = 3
    square_area = edge**2
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
    
    if not is_winner_decided and isDraw(round_count,game_round):
        display_results(player_mark_list,curr_player,player_mark_at-1, round_count,is_winner_decided)
    
if __name__ == '__main__':
    main()

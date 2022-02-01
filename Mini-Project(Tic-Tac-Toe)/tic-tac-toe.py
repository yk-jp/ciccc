user_input_constraint = {
    "lowest": 1,
    "highest": 9
}

win_pattern = [ 
  [0,1,2],
  [0,3,6],
  [0,4,8],
  [1,4,7],
  [2,4,6],
  [2,5,8],
  [3,4,5],
  [6,7,8]
]

# def flip_turn():


def user_input_validation():
    try:
        # type check
        user_input = int(input(f"Please make your move! [1-9]:"))
        # whether the input number is not out of range
        if not (user_input_constraint["lowest"] <= user_input <= user_input_constraint["highest"]):
            raise Exception

    except Exception:
        print('this is not a valid number. try again')

    return user_input

def draw_result(user_input_list):
    for i in range(len(user_input_list)):
        # ajust space
        if i%3 == 0:
            print('  ',end='')

        # get data from ele
        ele = str(user_input_list[i])
        # draw a mark
        print(ele, end=' ')

        # adjust layout
        if i % 3 != 2:
            print('|',end=' ')
        # create border
        if i%3 == 2 and i != len(user_input_list)-1:
            print('')
            print('','---|---|---')

def main():
    #default settings
    edge = 3
    square_area = edge**2
    user_input_list = [""] * square_area #str 

    # start the game
    print('Tic-Tac-Toe!')
    print('Player1 is 0 and Player2 is X.')


    
if __name__ == '__main__':
    # main()
    test_list = [0,0,0,0,0,0,0,0,0]
    draw_result(test_list)

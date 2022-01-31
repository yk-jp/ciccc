user_input_constraint = {
    "lowest": 1,
    "highest": 9
}

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
  for 
  print('|')

  print('---')





def main():
    #default settings
    edge = 3
    square_area = edge**2
    user_input_list = [] * square_area

    # start the game
    print('Tic-Tac-Toe!')
    print('Player1 is 0 and Player2 is X.')


if __name__ == '__main__':
    
    main()

""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    # your code goes here.
    print(answer)
    # binary search 
    lower = 0
    upper = 1000
    steps = 0
    guess_count = 0

    while lower <= upper:
        
        try:
          # type check
          guess_num = int(input(f"Enter your guess from {lower} to {upper}: "))
          # whether the input number is not out of range
          if not (lower <= guess_num <= upper):
            raise Exception
        except Exception:
          print('this is not a valid number. try again')

        steps += 1
        guess_count += 1
        if guess_num == answer:
            break
        elif guess_num < answer:
            lower = guess_num + 1
        else:
            upper = guess_num - 1
        
        print(f'Wrong! Guess count: {guess_count}')

    print(f'You got it! The hidden number is {answer}')
    print(f'It took you {guess_count} guess(es).')

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()

# reference 
# how to write try-exception statement
# https://docs.python.org/3/tutorial/errors.html
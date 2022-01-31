while True:  # This makes your code repeat forever,
    # to make it easier for you to keep testing it out with different values

    # You may assume the input will be valid
    # e.g. Your program does not have to work if someone gives an n that is
    #      bigger than the total number of digits in number. Your code must
    #      only work correctly for valid input.
    number = int(input("Please give an integer number: "))  # this asks the user for input and then stores the user
    # input as an int into our variable.
    n = int(input("Which position's digit do you want? "))

    print(".....YOUR CODE HERE......")  # TODO: Replace the filler text here with your code
    # edge case 

    res_digit = number

    div_count = 0
    
    while div_count < n-1 and res_digit > 0: # the edge case for digit out of bound
      # navigate to the n th digit
      res_digit//= 10
      div_count+=1
    
    print(f'{n}th digit of the {number}  is {res_digit % 10}') # return a remainder

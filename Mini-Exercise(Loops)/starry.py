def draw_space(count):
  i = 0
  # open a space
  while i < count:
    print(" ",end = '')
    i+=1

def draw_star(count):
  i = 0
  # open a space
  while i < count:
    print("*",end = '')
    i+=1

# What does the code below do? Write a comment explaining each line for Drawing 1.

n = int(input("Choose a number: "))

#   # Drawing Example
# for row in range(n):  # for each row
#     for column in range(row+1):  # for each column
#       print('*', end='')  # print without newline at the end
#     print()

  # Drawing 1
  # YOUR CODE BELOW (feel free to comment out previous drawings to make newer ones more clear)

print("----------  drawing1 ---------")
  # iterate for loop until h(height) reaches out to the end of layer.  
for h in range(1,n+1):
  # culuclate the number of space on the left side from the center line
  num_left_space = n-h
  # the number of star goes up by 2 such as 1 , 3 , 5. meaning that if this is represented by n, the end of the loop, The fomula should be 2 * h -1
  num_star = 2 * h - 1

  # open space
  draw_space(num_left_space)
  # draw a star
  draw_star(num_star)
  # to do a line break
  print("")  




print("----------  drawing2 ---------")
  # Drawing 2
for column in range(n,-1,-1): #decrease number from n to 1
  #draw as many star as the number of column
  draw_star(column)
  print("") #line break




# if n is even, see n as n + 1 to be odd
if n%2 == 0:
  n+=1

  # Drawing 3
print("----------  drawing3 ---------")

for row in range(1,n+1):
  num_star = row
  # decend the number in the middle to be synmetrical. 
  if (n + 1)//2 < row:
    num_star = n-row+1

  # draw stars
  draw_star(num_star)
  print("")
  
  # Drawing 4

  # Drawing 5
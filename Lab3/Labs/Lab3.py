"""
 String, List - Level 2.0
"""

def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    sum_hi = 0
    pattern = 'hi'

    for i in range(len(string)-1):
      if string[i:i+2] == pattern:
        sum_hi+=1
    return sum_hi 

def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat_count,dog_count = 0,0
    
    pattern = {
      "cat":"cat",
      "dog":"dog"
    }
    
    for i in range(len(string)-2):
      word = string[i:i+3]
      if word == pattern["cat"]:
        cat_count+=1
      elif word == pattern["dog"]:
        dog_count+=1
    return cat_count == dog_count
    


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    sum_code = 0
    pattern_first = "co"
    pattern_last_letter ="e" 
    for i in range(len(string)-3):
      if string[i:i+2] == pattern_first and string[i+3] == pattern_last_letter:
        sum_code+=1
    return sum_code 
    


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """ 

    compare_len = len(a) if len(a) < len(b) else len(b)
  
    lower_case_a = a.lower()
    lower_case_b = b.lower()
    
    for i in range(compare_len):
      
      if lower_case_a[-1-i] != lower_case_b[-1-i]:
        return False

    return True

def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    count = 0

    for num in nums:
      if num%2 == 0:
        count+=1

    return count


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    min_num = nums[0]
    max_num = nums[0]

    for num in nums:
      if num < min_num:
        min_num = num
      elif num > max_num:
        max_num = num

    return max_num - min_num 
      
def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    if len(nums) == 0: return 0

    sum_num = 0

    for i in range(len(nums)):
      if nums[i] == 13: 
         continue
      if(i>0 and nums[i-1] == 13):
         continue

      sum_num += nums[i]

    return sum_num

def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    
    sum_num = 0
    six_start = False
    for i in range(len(nums)):
      if nums[i] == 6:
        six_start = True
      if not six_start: 
        sum_num+=nums[i]
      
      if nums[i] == 7:
        six_start = False
    return sum_num


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """

    two_count = 0

    i = 0
    while i < len(nums) and two_count != 2:
      if nums[i] ==2:
        two_count+=1
      else:
        two_count = 0
      if two_count >=2:
        return True
        
      i+=1

    return False 
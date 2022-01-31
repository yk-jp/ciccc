"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    if 6 not in nums:
        return False

    six_at = nums.index(6)
    return six_at == 0 or six_at == len(nums)-1  


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    if not len(nums): return False

    return nums[0] == nums[-1]


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    sum = 0
    for num in nums:
        sum += num
    return sum


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    nums_len = len(nums)
    first_ele = nums[0]
    for i in range(1,nums_len):
        nums[i-1] = nums[i]
    nums[nums_len-1] = first_ele
    return nums

def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    nums_len = len(nums)
    for i in range(nums_len//2):
        temp = nums[i]
        nums[i] = nums[nums_len-1-i]
        nums[nums_len-1-i] = temp
    
    return nums
         

def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    num_replace_with = nums[0] if nums[0] > nums[-1] else nums[-1]
    return [num_replace_with] * len(nums)


def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    return [nums[0],nums[-1]]


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    return 2 in nums or 3 in nums

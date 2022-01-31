""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.

# asc = ascending order, dec = decending order
order_map = {
    'asc':'asc',
    'dec':'dec'
}

# create a function to reduce a redundancy with same sorting algorithm. 
def selection_sort(alist, order = 'asc'):
    for i in range(len(alist) - 1):
        swap_at = i
        for j in range(i + 1, len(alist)):
            #if order is ascending  
            if order_map[order] == 'asc':
                if alist[j] < alist[swap_at]:
                    swap_at = j 
            # if order is decending 
            elif order_map[order] == 'dec':
                if alist[j] > alist[swap_at]:
                    swap_at = j
        if swap_at != i:
            temp = alist[swap_at] 
            alist[swap_at] = alist[i]
            alist[i] = temp
    
    return alist

def sort_half(alist):
    if len(alist) < 2: return alist
    first_half_list = alist[0:len(alist)//2]
    second_half_list = alist[len(alist)//2:len(alist)]

    first_half_list = selection_sort(first_half_list,'asc')
    second_half_list =  selection_sort(second_half_list,'dec')
    return first_half_list + second_half_list

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.

def merge_two(A, B):
    index_A,index_B = 0, 0

    # generate a list with a total length of two of list.
    mergedList = [] * (len(A) + len(B))

    while index_A < len(A) and index_B < len(B):
        temp_ele = None

        if A[index_A] < B[index_B]:
            temp_ele = A[index_A]
            index_A +=1 #to compare next ele in A with current ele in B
        else:
            temp_ele = B[index_B]
            index_B+=1

        # add element in list 
        mergedList.append(temp_ele)
    
    # if A,B don't have same length of list each other, It's possible to remain elements that don't get compared with other's elements
    remainingList = A if index_A < len(A) else B
    index_at = index_A if remainingList == A else index_B

    # append remaining elements
    while index_at < len(remainingList):
        mergedList.append(remainingList[index_at])
        index_at+=1
    
    return mergedList


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    for i in range(len(mylist)):
        if mylist[i] < 0:
            mylist[i] = 0

    return mylist
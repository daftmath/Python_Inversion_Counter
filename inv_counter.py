__author__ = 'daftmath@gmail.com'

# Python implementation of merge sort with inversion counter in O(nlog(n)) time

# Input: A python class list with elements consisting of type int or float
# Output: A python class tuple where the first element is the sorted array
#         and the second element consists of the number of inversions

# Example Usage:
#  >>> from inv_counter import merge_sort_inv_count as merge_sort
#  >>> unsorted_list = [1, 3, 5, 2, 4, 6]
#  >>> sorted_list = merge_sort(unsorted_list)
#  >>> print(sorted_list)
#  >>> ([1, 2, 3, 4, 5, 6], 3)


def merge_sort_inv_count(array, inv_count=0):
    array_length = len(array)

    if array_length <= 1:
        return array, inv_count
    else:
        left = merge_sort_inv_count(array[0:array_length//2], inv_count)
        right = merge_sort_inv_count(array[(array_length//2):array_length+1], inv_count)
        inv_count = left[1] + right[1]
    return merge_split_subr(left[0], right[0], inv_count)


def merge_split_subr(left, right, inversions):
    s_array = []
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            s_array.append(left[i])
            i += 1
        else:
            s_array.append(right[j])
            j += 1
            inversions += (len(left)-i)
    if i >= j:
        s_array.extend(right[j:])
    else:
        s_array.extend(left[i:])
    return s_array, inversions

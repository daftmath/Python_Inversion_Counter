# Merge Sort and Inversion Counter
## O(nlog(n)) time

\__author__ = 'daftmath@gmail.com'

Python implementation of merge sort with inversion counter in O(nlog(n)) time

Input: A python class list with elements consisting of type int or float    
Output: A python class tuple where the first element is the sorted array
        and the second element consists of the number of inversions

Example Usage:    
  \>>>  from inv_counter import merge_sort_inv_count as merge_sort    
  \>>>  unsorted_list = [1, 3, 5, 2, 4, 6]    
  \>>>  sorted_list = merge_sort(unsorted_list)    
  \>>>  print(sorted_list)    
  \>>>  ([1, 2, 3, 4, 5, 6], 3)    

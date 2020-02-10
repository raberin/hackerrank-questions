'''
Given an array, seperate the values where subsetA's sum is greater than the rest of the arr
arr = [3,7,5,6,2]
subsetA = [7,6]
subsetA's sum is [6,7] =  13 which is higher than [3,5,2] = 9
Answer is [7,6]

Grab highest numbers, and keep adding the highest number UNTIL the sum of the subset is higher than the rest
'''


# Naive O(n^2)
def subsetA(arr):
    mapped = arr
    cache = {'subset_sum': 0}
    subset_a = []
    while cache['subset_sum'] < sum(mapped):
        # Grab 1st highest num
        biggest = mapped.index(max(mapped))
        cache['subset_sum'] += mapped[biggest]
        # Remove it and put in subset
        subset_a.append(mapped.pop(biggest))
    return sorted(subset_a)


# O(nlogn) - Time complexity Sorting
def subsetA_sort(arr):
    # Sort arr
    sorted_arr = sorted(arr)
    # Store biggest in subset_a
    subset_a = []
    sorted_arr_sum = sum(sorted_arr)
    subset_a_sum = 0
    while subset_a_sum <= sorted_arr_sum:
        # Pop value from sorted_arr
        popped = sorted_arr.pop()
        # Add popped into subset_a and add to subset_a_sum
        subset_a_sum += popped
        subset_a.append(popped)
        # Subtract popped from sum
        sorted_arr_sum -= popped
    return subset_a

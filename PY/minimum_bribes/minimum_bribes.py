# Test Case 1: No number can be > 2 spaces away from original
# Test Case 2: Any number can be

# O(n)


def minimum_bribes(arr):
    bribes = 0
    # Recreate arr by subtracting each value by 1 to make it more understanble of where it originally was
    updated_arr = [ele - 1 for ele in arr]
    for current, original in enumerate(updated_arr):
        # Check if the original - current > 2... its bribed more than 2x
        # If so print('Too chaotic') and return
        if original - current > 2:
            print("Too chaotic")
            return
        # Now check every value between current location -> original
        # Looping backwards from right to left
        # If the nums after P > P increment moves += 1
        for i in range(max(original - 1, 0), current):
            if updated_arr[i] > original:
                bribes += 1
    print(bribes)


print(minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]))

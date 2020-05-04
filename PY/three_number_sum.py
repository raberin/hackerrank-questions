def threeNumberSum(arr, target):
    # Create a hashtable to store needed_num : (first_num, second_num)
    hashmap = {}
    # Create a list to return
    sums = set()
    # Loop through arr
    for i in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[i] == arr[j]:
                continue
            # Add both nums and subtract from target
            print(arr[i], i, arr[j], j)
            print(f"arr[i] + arr[j] = {arr[i] + arr[j]}")
            needed_num = target - (arr[i] + arr[j])
            # Store key:value in hash
            hashmap[needed_num] = [arr[i], arr[j]]
    # Loop one more time...
    print(hashmap)
    for i in range(len(arr)):
        # check if key is in arr
        if arr[i] in hashmap:
            print(f"arr[i] = {arr[i]}, hashmap[arr[i]]={hashmap[arr[i]]}")
            # form list and sort
            sum = hashmap[arr[i]].copy()
            sum.append(arr[i])
            sum = sorted(sum)
            # Add
            sums.add(tuple(sum))
    sums = list(sums)
    sums = [list(tup) for tup in sums]
    return sorted(sums)

# Incomplete solution... Needs work on handling same keys on set


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

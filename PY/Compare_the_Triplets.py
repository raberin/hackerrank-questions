# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result = [0, 0]
    for x in range(0, 3):
        if a[x] > b[x]:
            result[0] += 1
        elif b[x] > a[x]:
            result[1] += 1
    return result

def diagonalDifference(arr):
    result = 0
    leftDiag = 0
    rightDiag = 0
    leftPointer = 0
    rightPointer = len(arr) - 1
    for ele in arr:
        leftDiag += ele[leftPointer]
        leftPointer += 1
        rightDiag += ele[rightPointer]
        rightPointer -= 1
    result = leftDiag - rightDiag
    return abs(result)


square = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(square))

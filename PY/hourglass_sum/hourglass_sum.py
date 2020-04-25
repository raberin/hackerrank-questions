import random

# Code to make matrices with random numbers in it


def make_matrix(size):
    matrix = []
    for y in range(size):
        row = [None] * 6
        for x in range(size):
            row[x] = random.randint(1, 10)
        matrix.append(row)
    return matrix


my_matrix = [[7, 2, 4, 9, 4, 8],
             [7, 3, 2, 7, 6, 8],
             [3, 1, 2, 9, 9, 2],
             [3, 6, 2, 6, 10, 9],
             [5, 4, 5, 10, 4, 6],
             [4, 1, 10, 8, 2, 9]]


def hourglassSum(matrix):
    # Create a matrix with a size of 4
    sums = [[0] * 4 for i in range(4)]
    # Loop through y
    for y in range(4):
        # Loop through x
        for x in range(4):
            # Sum top half
            sums[y][x] += matrix[y][x]
            sums[y][x] += matrix[y][x + 1]
            sums[y][x] += matrix[y][x + 2]
            # Sum center
            sums[y][x] += matrix[y + 1][x + 1]
            # Sum bottom half
            sums[y][x] += matrix[y + 2][x]
            sums[y][x] += matrix[y + 2][x + 1]
            sums[y][x] += matrix[y + 2][x + 2]
    # Flatten sums and grab max num
    return max([num for row in sums for num in row])

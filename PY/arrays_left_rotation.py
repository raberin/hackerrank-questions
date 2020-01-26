"""
input: [arr], int(how many times you want to rotate)
output: [rotated arr]

example: 
intput: [1,2,3,4,5], 1 
output: [2,3,4,5,1]

example 2: 
intput: [1,2,3], 1 
output: [3,2,1], 2
"""


def rot_left(arr, num):
    result = arr
    for i in range(num):
        result.append(result.pop(0))
    return arr

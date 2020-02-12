"""
Given an array of negative, positive, and 0 integers. 
Divide each type of number by the length of the array. 
Print out each type of integers difference in a new line

EX:
    Input: [1,1,0,-1,-1] 
    Explanation: 2 positive, 2 negative, 1 zero => 2/len(arr), 2/len(arr), 1/len(arr)
    Output:0.40000 \n 0.40000 \n 0.20000
"""

# Complete the plusMinus function below.


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num == 0:
            zero += 1
        else:
            negative += 1
    positive = round(positive / len(arr), 6)
    negative = round(negative / len(arr), 6)
    zero = round(zero / len(arr), 6)
    print(positive)
    print(negative)
    print(zero)

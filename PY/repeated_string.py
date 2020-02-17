"""
Given a string and an integer, count how many occurences of 'a' that occur from the 0th index all the way up to the n index

EX:
repeated_string('abcac',10) => 'abcacabcac' == 4 a's occured
repeated_string('a', 100000) => 'aaaaaa....'  == 100000 a's
"""


def repeatedString(s, n):
    # Basecase if string is just 'a'
    if s == 'a':
        return n
    # Counter and create new_string
    count = 0
    new_string = ''
    # Loop and concat substring
    for i in range(n):
        new_string += s
    # Count how many occurences
    for i in range(n):
        if new_string[i] == 'a':
            count += 1
    return count

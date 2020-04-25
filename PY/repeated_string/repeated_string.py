"""
Given a string and an integer, count how many occurences of 'a' that occur from the 0th index all the way up to the n index

EX:
repeated_string('abcac',10) => 'abcacabcac' == 4 a's occured
repeated_string('a', 100000) => 'aaaaaa....'  == 100000 a's
"""


def repeatedString(s, n):
    # Count how many 'a' in s
    a_in_s = s.count('a')
    # Get how many times str repeats
    num_of_repeats = n // len(s)
    # Slice off the remainder str and get count
    remainder_str = s[:n % len(s)]
    remainder_a = remainder_str.count('a')
    return a_in_s * num_of_repeats + remainder_a

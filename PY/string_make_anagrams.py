"""
Given two strings, determine the minimum number of character deletions to make the strings an anagram

input: cde, abc
output: 4 - delete 'de' and 'ab'

"""


def make_anagram(s1, s2):
    sort1 = sorted(list(s1))
    sort2 = sorted(list(s2))

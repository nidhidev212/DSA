# -*- coding: utf-8 -*-
"""count vowel in string using recursion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oCV-mzXRwcCvbKdki2GKnAFEPSt78JA9
"""

def count_vowels(s):
    if s == "":
        return 0
    elif s[0].lower() in 'aeiou':
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

print(count_vowels("nidhi dev"))
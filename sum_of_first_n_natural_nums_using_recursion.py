# -*- coding: utf-8 -*-
"""sum of first n natural nums using recursion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m8pvq7y9qR98UPRf9Nqej8NIzTY7RC4W
"""

def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

print(sum_natural_numbers(5))


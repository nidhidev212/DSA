# -*- coding: utf-8 -*-
"""example 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UGced4B9QMRQzGGtpiQCuWe9Y4K463Hn
"""

def iseven(n):
# Base case for even number
 if n == 0:
   return True
# Base case for odd number
 elif n == 1:
  return False
# Recursive case
 elif n > 1:
  return isodd(n - 1)
# Handle negative numbers
 elif n < 0:
  return iseven(-n)
def isodd(n):
  return not iseven(n)
# Input from the user
num = -5
if iseven(num):
 print("The number is even")
else:
 print("The number is odd")


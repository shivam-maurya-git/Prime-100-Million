# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18rQqAmc1GczfftRO3K-kyxzqTZHRkHQn
"""

import numpy as np
import math

def prime_or_not(num):
  num_check = int(math.sqrt(num))
  x = np.linspace(2,num_check,num = num_check-1)
  rem = num%x
  if 0 not in rem:
    return num

prime = list()
for i in range(2,10000000):
   if prime_or_not(i)!= None:
     prime.append(prime_or_not(i))
print(prime)


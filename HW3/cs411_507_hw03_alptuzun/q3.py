# -*- coding: utf-8 -*-
"""Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JlH9HicsusyM3MlTZ-9I5iXWmzLQk3hX
"""

LCx1 = 2**60 - 1
LCx2 = 2**95 - 1
LCx3 = 2**97 - 1
LCx4 = 2**75 - 1

LC = LCx1 + (LCx1 * LCx2) + (LCx2 * LCx3) + (LCx2 * LCx3 * LCx4) + (LCx1 * LCx2 * LCx3 *LCx4)

print(LC)

from math import gcd
a = [LCx1, LCx2, LCx3, LCx4]
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)
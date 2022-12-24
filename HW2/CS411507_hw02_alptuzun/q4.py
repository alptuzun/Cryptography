# -*- coding: utf-8 -*-
"""Q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NEo1rjY4PX6fOQ55404Z3BE8ue0ZJdk
"""

import math
import random
import warnings
import sympy

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def linearCongruence(a, b, n):
    a = a % n
    b = b % n
    x = y = 0
  
    #use the extended euclidean algorithm to solve for x, y and gcd  
    gcd, x, y = egcd(a, n)
     
    if (b % gcd != 0):
        print("There isn't any solution!")
        return
     
    x0 = (x * (b // gcd)) % n
    if (x0 < 0):
        x0 += n
     
    # if there are multiple solutions, print all of them
    print("Solutions for x: ")
    for i in range(gcd):
        print((x0 + i * (n // gcd)) % n, end = "\n")

"""ax = b mod (n)"""

n1 = 1593089977489628213419978935847037520292814625191902216371975
a1 = 1085484459548069946264190994325065981547479490357385174198606
b1 = 953189746439821656094084356255725844528749341834716784445794

linearCongruence(a1, b1, n1)

n2 = 1604381279648013370121337611949677864830039917668320704906912
a2 = 363513302982222769246854729203529628172715297372073676369299
b2 = 1306899432917281278335140993361301678049317527759257978568241

linearCongruence(a2, b2, n2)

n3 = 591375382219300240363628802132113226233154663323164696317092
a3 = 1143601365013264416361441429727110867366620091483828932889862
b3 = 368444135753187037947211618249879699701466381631559610698826

linearCongruence(a3, b3, n3)

n4 = 72223241701063812950018534557861370515090379790101401906496
a4 = 798442746309714903219853299207137826650460450190001016593820
b4 = 263077027284763417836483401088884721142505761791336585685868

linearCongruence(a4, b4, n4)
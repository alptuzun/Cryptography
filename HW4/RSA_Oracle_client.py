import random
import requests
import math
from random import randint

API_URL = 'http://10.92.55.4:6000'
my_id = 28991

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
def RSA_Oracle_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id)) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())

def RSA_Oracle_Query(c_):
  response = requests.get('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Query", my_id, c_)) 
  print(response.json())
  m_= ""
  if response.ok:	m_ = (response.json()['m_'])
  else: print(response)
  return m_

def RSA_Oracle_Checker(m):
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Checker", my_id, m))
  print(response.json())

## THIS IS ONLY AN EMPTY CLIENT CODE, YOU HAVE TO EXTRACT M
## THEN CHECK IT USING THE CHECKING ORACLE.

c, N, e = RSA_Oracle_Get()

# In this question, they wanted from us to do a chosen ciphertext attack and with Deterministic property of RSA, we can deduct the plaintext from multiple ciphertext that can be querried to the oracle.
# to start we should choose a random number that is in Zn* group for N. Example = 3
r = 3 
print("GCD of 3 and N is: ", math.gcd(r, N))
# because the gcd = 1, we can use this random number to extract information
# compute c_ = c*(r^e) mod n 
c_ = (pow(r, e) * c) % N
print("c_ is :", c_)
#querry to find the corresponding plaintext for c_
m_ = RSA_Oracle_Query(c_)
# get the modular inverse of the random r to extract the m
m = (m_ * modinv(r, N)) % N
plaintext = m.to_bytes((m.bit_length() // 8 + 1), byteorder="big").decode()
# The hidden message is: Bravo! You found it. Your secret code is 72375
print("The hidden message is: ", plaintext)
RSA_Oracle_Checker(plaintext)
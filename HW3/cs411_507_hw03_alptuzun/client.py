import random
import requests
import BitVector

API_URL = 'http://10.92.55.4:6000'
my_id = 28991
def get_poly():
  endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
  response = requests.get(endpoint) 	
  a = 0
  b = 0
  if response.ok:	
    res = response.json()
    print(res)
    return res['a'], res['b']
  else:
    print(response.json())

def check_mult(c):
  #check result of part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
  response = requests.put(endpoint) 	
  print(response.json())

def check_inv(a_inv):
  #check result of part b
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
  print(response.json())

a, b = get_poly()
##SOLUTION

irreducible = BitVector.BitVector(bitstring='100011011')
n = 8
a_bit = BitVector.BitVector(bitstring=a)
b_bit = BitVector.BitVector(bitstring=b) 

q1 = a_bit.gf_multiply_modular(b_bit, irreducible, n)
check_mult(q1)
q2 = a_bit.gf_MI(irreducible, n)
check_inv(q2)
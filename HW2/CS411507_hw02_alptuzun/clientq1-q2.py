import random
import requests
import math

API_URL = 'http://10.92.55.4:6000'

# Change your id here
my_id = 28991

def getQ1():
    endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id)
    response = requests.get(endpoint)
    if response.ok:
        res = response.json()
        print(res)
        n, t = res['n'], res['t']
        return n, t
    else:
        print(response.json())

def checkQ1a(order):  # check your answer for Question 1 part a
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
    response = requests.put(endpoint)
    print(response.json())

def checkQ1b(g):  # check your answer for Question 1 part b
    # gH is generator of your subgroup
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g)
    response = requests.put(endpoint)  # check result
    print(response.json())

def checkQ1c(gH):  # check your answer for Question 1 part c
    # gH is generator of your subgroup
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH)
    response = requests.put(endpoint)  # check result
    print(response.json())

def getQ2():
    endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id)
    response = requests.get(endpoint)
    if response.ok:
        res = response.json()
        e, cipher = res['e'], res['cipher']
        return e, cipher
    else:
        print(response.json())

def checkQ2(ptext):  # check your answer for Question 2
    response = requests.put(
        '{}/{}'.format(API_URL, "checkQ2"), json={"ID": my_id, "msg": ptext})
    print(response.json())

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def generatorClass(n):
    s = set(range(1, n))
    res = []
    for a in s:
        g = set()
        for x in s:
            g.add(pow(a, x, n))
        if g == s:
            res.append(a)
    return res

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

# get the first question
n, t = getQ1()
# Z*n's elements are the results of the phi(958) so we need to input the function
checkQ1a(phi(n))
# empty initial array
genZ = []
# a generator that generates the class for Z*958 elements
gens = generatorClass(479)
for x in gens:
    if(gcd(x, 958) == 1):
        genZ.append(x)
print(genZ)
# Let's put 13 for this example for generator class
checkQ1b(13)
# empty initial array
genZ2 = []
# a generator that generates the class for Z*958 subgroup elements
gens2 = generatorClass(239)
if gens2:
    print(gens2)
# Let's put 7 this time to the input
checkQ1c(7)
# harcode the #'s in second question
p = 129711420978537746088867309342132426785901989689874594485896371555019986573705426172788805726178509467748040679168734095884433597017604012172054368990172572715857537355524013819947862920969421702067385445122242673064958991968666138544380365520456029952414962028711806175784928131826127885820644091951344318387
q = 174066672405085972657808881778978520582809763235147358374332409966322987290745416405220414323004782906757362579157117914494927198442645581197584273451379119673753279114693557694861941678350357667191083878100828920198503774539271289263633646647364198130180304138099281532660260760636194367337370132530987351081
n = p*q
# get the second question
e, c = getQ2()
# Easy formula for calculating the phi(n) if n consists of two prime numbers
phiN = (p-1)*(q-1)
#get the modular inverse for finding element d
d = modinv(e, phiN)
# easy python built-in power method for modular binary exponentiation
m = (pow(c, d, n))
# for converting the integer to byte string
px = m.to_bytes((m.bit_length() // 8 + 1), byteorder='big')
#decoding the byte string
plaintext = px.decode('UTF-8')
print("The plaintext: ", plaintext)
#sending the answer
checkQ2(plaintext)
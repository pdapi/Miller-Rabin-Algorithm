import random
import gmpy2
import os, sys
from gmpy2 import mpz

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from miller_rabin import *
system_random = random.SystemRandom()

# getting systemRandom instance out of random class
system_random = random.SystemRandom()

# Secure random number
test = (system_random.randint(1, 3000000000000000000000000000000000000000000000000000000000000000000000000))
print(test)
# Output 22
#val = gmpy2.mpz(test)
#gmpy2.c_divmod()
#test = gmpy2.mpz(7)
print(gmpy2.c_mod(test, 2))
if (gmpy2.c_mod(test, 2) == 0) :
    print("test")

print("fdfdf")
print(gmpy2.c_div(50, 2))

a = system_random.randint(1, 340282366920938463463374607431768211455)
b = system_random.randint(1, 340282366920938463463374607431768211455)
c = system_random.randint(1, 340282366920938463463374607431768211455)
print(a, b, c)
print(gmpy2.powmod(a, b, b))

#print(puissance_mod(a, b, c))
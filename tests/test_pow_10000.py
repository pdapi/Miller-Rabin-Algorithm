import sys, os
import random
import gmpy2
from gmpy2 import mpz

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from miller_rabin import *
system_random = random.SystemRandom()

# PROGRAMME DE TEST DE LA FONCTION D'EXPONENTIATION MODULAIRE SUR 10 000 VALEURS #

def test_grand():
    try:
        for i in range(0, 1000, 1):
            exposant =  gmpy2.mpz(system_random.randint(1, 1000000))
            base  = gmpy2.mpz(system_random.randint(1, 1000000))
            modulo = gmpy2.mpz(system_random.randint(1, 1000000))

            result = puissance_mod(base, exposant, modulo)

            # on regarde si il y'a une différence entre la fonction fournie et la notre
            if (result != gmpy2.powmod(base, exposant, modulo)):
                print("erreur nombres différents")
            else :
                print("test ", i+1,"/1000  ->  ok")

    except KeyboardInterrupt:
        print(" Ctrl + c pressed, goodbye !")



if __name__ == "__main__":
    test_grand()
    sys.exit()
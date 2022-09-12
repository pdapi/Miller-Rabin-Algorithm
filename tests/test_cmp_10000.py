import sys, os
import random
import gmpy2
from gmpy2 import mpz

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from miller_rabin import *
system_random = random.SystemRandom()

# PROGRAMME DE TEST DE LA FONCTION DECOMPOSITION SUR 10 000 VALEURS #

def test_petit():
    try:
        for i in range(0, 10000, 1):
            val =  system_random.randint(1, 100000000000000000)
            result = comp(val)
            if (val-1 != 2**result[1]*result[0]):
                print(f"erreur nombres différents 2^{result[1] : < 3}  * {result[0] : < 20} != {val : < 20}")
            if (result[0]%2 == 0):
                print("erreur d est pair")
            #else :
                #print("test ", i+1,"/1000  ->  ok")


    except KeyboardInterrupt:
        print(" Ctrl + c pressed, goodbye !")

def test_grand():
    try:
        for i in range(0, 10000, 1):
            val =  gmpy2.mpz(system_random.randint(1, 12301866845301277551304949583849627207728535695953347921973224521517264005072636575187452021997864693899564749427740638459251925573263034537315482685079170261221429134616704219214311602221240479274737794080665351419597459856902143413))
            result = comp(val)
            if (val-1 != 2**result[1]*result[0]):
                print(f"erreur nombres différents 2^{result[1] : < 3}  * {result[0] : < 20} != {val : < 20}")
            if (result[0]%2 == 0):
                print("erreur d est pair")
            else :
                print("test ", i+1,"/1000  ->  ok")


    except KeyboardInterrupt:
        print(" Ctrl + c pressed, goodbye !")



if __name__ == "__main__":
    test_grand()
    sys.exit()
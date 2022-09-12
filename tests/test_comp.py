import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from miller_rabin import *

# PROGRAMME DE TEST POUR LA FONCTION DE DECOMPOSITION #

def testCmp(val):
    result = comp(val)
    if (result[0] != -555):
        #print(f"d = {result[0] : <10} 2^{result[1] : <10}")
        print(val, "- 1 = ", "2^", result[1], " * ", result[0])
    else:
        print("no result")

def main():
    try:
        while True:
            print("Entrez un nombre : ")
            number = int(input())
            testCmp(number)
            
            
    except KeyboardInterrupt:
        print(" Ctrl + c pressed, goodbye !")

if __name__ == "__main__":
    main()
    sys.exit()
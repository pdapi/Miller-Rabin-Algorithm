import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from miller_rabin import *

def test_nb(t):
    if (miller_rabin(t, 20) == '0'):
        print("nombre composé \n")
    else:
        print("nombre probablement premier \n")

# TEST DES TROIS ENTIERS DE LA QUESTION 6
def test_mill():
    n1 = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF
    print(n1)
    test_nb(n1)

    n2 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEC4FFFFFDAF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000002D9AB
    print(n2)
    test_nb(n2)

    n3 = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
    print(n3)
    test_nb(n3)

# TEST DE LA FONCTION DU NOMBRE D'ITERATION NECESSAIRE POUR TROUVER UN NOMBRE PREMIER (EVALUATION)
def test_eval():
    result = eval(4096, 20)
    print(result)

# TEST 100x LA FONCTION EVALUATION RENVOIE LA MOYENNE
def moy_100():
    result = 0
    for i in range(0, 100, 1):
        evaluation = eval(4096, 20)
        print(evaluation)
        result += evaluation
    
    print("moyenne : ", result/100)

def main():
    test_mill()
    #test_eval()
    #moy_100()

if __name__ == "__main__":
    main()
    sys.exit()
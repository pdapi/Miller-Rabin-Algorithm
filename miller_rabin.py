import random
from re import T
import secrets
import sys
import math
import gmpy2
from gmpy2 import mpz
# getting systemRandom instance out of random class
system_random = random.SystemRandom()

########## FONCTION DECOMPOSITION ##########
# entrée  : entier n
# sortie  : val, cmp
# but     : deux valeurs telles que 2^cmp * val = n-1
def comp(n) :
    verif = 0
    cmp = 0
    val = gmpy2.mpz(n-1)

    if (gmpy2.c_mod(val, 2) != 0) :
        return [n-1, 0]

    while(verif == 0):
        if (gmpy2.c_mod(val, 2) == 0):
            val = gmpy2.c_div(val, 2)
            cmp+=1
        else:
            verif=1

    return [val, cmp]
############################################


def puissanceRecursive(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return puissanceRecursive(x * x, n / 2)
    else:
        return x * puissanceRecursive(x * x, (n - 1) / 2)

########## FONCTION D'EXPONENTIATION MODULAIRE ##########
# entrée  : entier a 
#           entier t (puissance)
#           entier n (modulo)
# sortie  : a^t (mod n)
def puissance_mod(a, t, n):
    if (t == 1):
        return gmpy2.c_mod(gmpy2.mpz(a), gmpy2.mpz(n))
    if (gmpy2.c_mod(gmpy2.mpz(t), 2) == 0):
        return puissance_mod(gmpy2.mpz(a)**2, gmpy2.c_div(gmpy2.mpz(t), 2), gmpy2.mpz(n))%n
    if (gmpy2.c_mod(gmpy2.mpz(t), 2) != 0):
        return gmpy2.mul(gmpy2.mpz(a), puissance_mod(gmpy2.mpz(a)**2, gmpy2.c_div(gmpy2.mpz(t-1), 2), gmpy2.mpz(n)))%gmpy2.mpz(n)
#########################################################


########## IMPLEMENTATION DU TEST DE MILLER RABIN ##########
# Fonction secondaire
# Effectue un seul tour de l'algorithme
def miller_tmp (n):
    #recuperation de n-1 = 2^s * d
    result = comp(n)
    s = result[1]
    d = result[0]

    #tirage aléatoire de a
    a = system_random.randint(2, n-1)

    #calcul de la puissance modulaire
    popomod = gmpy2.powmod(gmpy2.mpz(a), gmpy2.mpz(d), gmpy2.mpz(n))
    if (popomod == 1 or popomod == -1):
        return False

    #Boucle
    for i in range(1, s, 1):
        result = gmpy2.powmod(gmpy2.mpz(a), (gmpy2.mpz(d)*2**gmpy2.mpz(i)), gmpy2.mpz(n))
        if (result == -1):
            return False
        if (result == 1):
            return True

    result = gmpy2.powmod(gmpy2.mpz(a), (gmpy2.mpz(d)*2)**gmpy2.mpz(s), gmpy2.mpz(n))
    if (result == 1):return False
    else: return True

# Fonction principale
# entrée  : entier n
#           entier cpt (nombre d'itération)
# sortie  : 0 si n est composé || 1 si n est probablement premier
def miller_rabin(n, cpt):
    for i in range(0, cpt, 1):
        if (miller_tmp(n) == True):
            return '0'
    return '1'
       
########## FIN IMPLEMENTATION DU TEST DE MILLER RABIN ##########

########## FONCTION D'EVALUATION ##########
# entrée  : nombre de bits b
#           entier cpt (nombre d'itération)
# sortie  : retourne le nombre d'itération pour trouver un nombre premier
# but     : on tire un nombre aléatoire de b bits, tant que celui-ci n'est pas premier
#           on retire un nouveau nombre aléatoire de b bits. Lorsque l'on trouve un
#           nombre premier on renvoie le nombre d'essais qui ont été effectués
def eval(b, cpt):
    compteur = 0
    alea = secrets.randbits(b)

    while (miller_rabin(alea, cpt) == '0'):
        compteur +=1
        alea = secrets.randbits(b)
    return compteur
######## FIN FONCTION D'EVALUATION ########


if __name__ == "__main__":
    sys.exit()


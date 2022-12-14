# Fonction qui brut force diffie helman:
from math import sqrt
import math
from Chrono import Chronometre
from affinne import calculer_PGCD
from fonction import est_francais_simple


def test_brute_force(Ay: int, p: int, g: int):
    """ Brute force pour trouver la clé secrète
    Args:
        Ay (int): clé publique de A
        p (int): le p de la clé publique
        g (int): le g de la clé publique
    Returns:
        int: la clé secrète de A
    """
    chrono = Chronometre()
    for ind in range(1,p):
        if Ay == g**ind%p:
            chrono.stop()
            return ind
    return -1

# Calculez la valeur de la clé secrète a en utilisant la méthode baby step big step
def baby_step_giant_step(g, p, Ax):
    """ Methode baby step giant step pour trouver la clé secrète

    Args:
        g (int): le g de la clé publique
        p (int): le p de la clé publique
        Ax (int): clé partagé   

    Returns:
        int: la clé secrète partagé
    """
    chrono = Chronometre()
    m = int(math.ceil(math.sqrt(p)))
    baby_steps = [pow(g, i, p) for i in range(m)]
    for j in range(m):
        big_step = (Ax * pow(g, j * m, p)) % p
        if big_step in baby_steps:
            chrono.stop()
            return (j * m + baby_steps.index(big_step)) % p
    return -1

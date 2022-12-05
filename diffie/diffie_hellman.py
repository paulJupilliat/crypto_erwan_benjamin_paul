from math import sqrt
from random import randint

from .Personne import Personne


def est_premier(n):
    """Renvoie True si n est premier, False sinon
    Args:
        n (int): un entier
    Returns:
        bool: True si n est premier, False sinon
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def genere_nombre_premier(max):
    """Génère un nombre premier inférieur à max
    Args:
        max (int): un entier
    Returns:
        int: un nombre premier inférieur à max
    """
    n = randint(2, max)
    while not est_premier(n):
        n = randint(2, max)
    return n

def diffie_hellman():
    """Algorithme de Diffie-Hellman
    """
    # Initialisation des deux personnes
    personne1 = Personne()
    personne2 = Personne()

    # Génération de la clé publique
    p = genere_nombre_premier(100)
    g = genere_nombre_premier(p-1)

    # On envoie la clé publique à chaque personne
    personne1.set_cle_publique((g, p))
    personne2.set_cle_publique((g, p))

    # Génère et échange les clés
    personne1.set_cle_partagee(personne2.genere_echange())
    personne2.set_cle_partagee(personne1.genere_echange())

    # Calcul de la clé partagée
    personne1.genere_cle()
    personne2.genere_cle()
    
    # retourne les personnes pour les utiliser 
    return personne1, personne2


diffie_hellman()

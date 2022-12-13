# Fonction qui brut force diffie helman:
from Chrono import Chronometre
from affinne import calculer_PGCD
from fonction import est_francais_simple
# from diffie_hellman import diffie_hellman_generation_cle


def brut_force_diffie_hellman_v1(message: str, len_cle: int) -> tuple[str, int]:
    """Brut force diffie hellman en connaissant la longueur de la clé si message codé avec césar
    Args:
        message (str): le message à décoder
        len_cle (int): la longueur de la clé
    Returns:
        str: le message décodé
        int: la clé
    """
    chrono = Chronometre()
    for i in range(1, int("9"*len_cle)):
        # chrono.affiche_chrono()
        message_decode = ""
        for lettre in message:
            message_decode += chr(ord(lettre) // i)
        if est_francais_simple(message_decode):
            chrono.stop()
            return message_decode, i
    return "pas trouvé"


def brut_force_diffie_hellman(message: str, len_cle_a: int, Ax: int, len_cle_b: int, By: int, p: int, g: int) -> tuple[str, int]:
    """Trouve le clé secrète des deux poersonnes
    Args:
        message (str): le message à décoder
        len_cle_a(int): longuer de la clé de la personne 1
        Ax(int): clé échangé par la personne 1 à la personne 2
        len_cle_b(int): longuer de la clé de la personne 2
        Ax(int): clé échangé par la personne 2 à la personne 1
        p(int): premier élément de la clé publique 
        g(int : deuxième élèment de la clé publique

    Returns:
        int: la clé
        int: la clé
    """
    chrono = Chronometre()
    # Cherche à avoir la clé secrète de la personne 1
    a = None
    b = None
    len_plus_g = max([len_cle_a, len_cle_b])  # Prend la clé la plus grande
    plus_g_nb = int("9"*len_plus_g)
    for ind in range(0, plus_g_nb):
        val_obtenu = pow(g, ind, p)
        if len_cle_a < ind and val_obtenu == Ax and calculer_PGCD(Ax, ind) == 1:
            a = ind
            if b != None:
                break
        if len_cle_b < ind and val_obtenu == By:
            b = ind
            if a != None:
                break
        print(ind)
    print(Ax, By)
    print(f"Ax = {Ax} g={g} a={a} p={p} == ")
    return a, b

def test_brute_force(len_cle_a: int, Ay: int, len_cle_b: int, By: int, p: int, g: int):
    for ind in range(1,p):
        if Ay == g**ind%p:
            return ind
    return (-1,0)

# Ay = pow(10,15,37)
# print(pow(10,3,37))
# print(test_brute_force(2,Ay,2,23,37,10))

# def brut_force_diffie_hellman_encode(message: str, len_cle: int) -> tuple[str, int]:
#     """Brut force diffie hellman en connaissant la longueur de la clé
#     Args:
#         message (str): le message à décoder
#         len_cle (int): la longueur de la clé
#     Returns:
#         str: le message décodé
#         int: la clé
#     """
#     chrono = Chronometre()
#     for i in range(1, int("9"*len_cle)):
#         # chrono.affiche_chrono()
#         message_decode = ""
#         for lettre in message:
#             message_decode += chr(ord(lettre) ** i)
#         if est_francais_simple(message_decode):
#             chrono.stop()
#             return message_decode, i
#     return "pas trouvé"


# def meet_middle(message: str, Xa: int, Yb: int) -> tuple[str, int]:
#     """Permet de cracker diffie hellman en utilisant meet middle

#     Args:
#         message (str): le message à décoder
#         Xa (int): La clé partagée par A
#         Yb (int): La clé partagée par B

#     Returns:
#         tuple[str, int]: le message décodé, la clé
#     """
#     personne1, personne2, Xa, Yb = diffie_hellman_generation_cle()
#     possibility1 = {}
#     possibility2 = {}
#     for i in range(1, 100000):
#         possibility1.add(brut_force_diffie_hellman(message, i))
#         possibility2.add(brut_force_diffie_hellman_encode(message, i))
#     for elmt in possibility1:
#         if elmt in possibility2:
#             return elmt, possibility2[elmt]

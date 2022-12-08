# Fonction qui brut force diffie helman:
from Chrono import Chronometre
from diffie_hellman import diffie_hellman_generation_cle
from fonction import est_francais_simple

def brut_force_diffie_hellman(message: str, len_cle: int) -> tuple[str, int]:
    """Brut force diffie hellman en connaissant la longueur de la clé
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


def brut_force_diffie_hellman_encode(message: str, len_cle: int) -> tuple[str, int]:
    """Brut force diffie hellman en connaissant la longueur de la clé
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
            message_decode += chr(ord(lettre) ** i)
        if est_francais_simple(message_decode):
            chrono.stop()
            return message_decode, i
    return "pas trouvé"


def meet_middle(message: str, Xa: int, Yb: int) -> tuple[str, int]:
    """Permet de cracker diffie hellman en utilisant meet middle

    Args:
        message (str): le message à décoder
        Xa (int): La clé partagée par A
        Yb (int): La clé partagée par B

    Returns:
        tuple[str, int]: le message décodé, la clé
    """
    personne1, personne2, Xa, Yb = diffie_hellman_generation_cle()
    possibility1 = {}
    possibility2 = {}
    for i in range(1, 100000):
        possibility1.add(brut_force_diffie_hellman(message, i))
        possibility2.add(brut_force_diffie_hellman_encode(message, i))
    for elmt in possibility1:
        if elmt in possibility2:
            return elmt, possibility2[elmt]


# Fonction qui brut force diffie helman:
from Chrono import Chronometre
from ..fonction import est_francais_simple


def brut_force_diffie_hellman(message: str, len_cle: int) -> str:
    """Brut force diffie hellman en connaissant la longueur de la clé
    Args:
        message (str): le message à décoder
        len_cle (int): la longueur de la clé
    Returns:
        str: le message décodé
    """
    chrono = Chronometre()
    for i in range(2**len_cle):
        chrono.affiche_chrono()
        message_decode = ""
        for lettre in message:
            message_decode += chr(ord(lettre) - i)
        if est_francais_simple(message_decode):
            chrono.stop()
            return message_decode
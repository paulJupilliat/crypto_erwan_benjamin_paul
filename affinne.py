import math
import string
import cesar

FRENQUENCE_FRANCAIS = {
    'A': 7.636,
    'B': 0.901,
    'C': 3.260,
    'D': 3.669,
    'E': 14.715,
    'F': 1.066,
    'G': 0.866,
    'H': 0.737,
    'I': 7.529,
    'J': 0.613,
    'K': 0.074,
    'L': 5.456,
    'M': 2.968,
    'N': 7.095,
    'O': 5.796,
    'P': 2.521,
    'Q': 1.362,
    'R': 6.693,
    'S': 7.948,
    'T': 7.244,
    'U': 6.311,
    'V': 1.838,
    'W': 0.049,
    'X': 0.427,
    'Y': 0.128,
    'Z': 0.326
}
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
premier26 = [1,3,5,7,9,11,13,15,17,23,21,25,19]

def tableau_frequence(texte : str) -> 'dict[str,int]':
    """donne le nombre d'apparation de chaque lettre du texte

    Args:
        texte (str): le texte

    Returns:
        dict[str,int]: le nombre d'apparition de chaque lettre dans le texte
    """
    res = {}
    for lettre in [ord(char.upper()) for char in clean(texte)]:
        if lettre >= 65 and lettre <= 90:
            if chr(lettre) not in res.keys():
                res[chr(lettre)] = 0
            res[chr(lettre)] += 1
    return res

def distance_texte(texte : str) -> int:
    """donne la distance du texte par rapport au fréquence habituel du français

    Args:
        texte (str): le texte

    Returns:
        int: le distance du texte
    """
    tableau_freq = tableau_frequence(texte)
    distance = 0
    for lettre in FRENQUENCE_FRANCAIS:
        if lettre in tableau_freq:
            distance += (
                FRENQUENCE_FRANCAIS[lettre] - tableau_freq[lettre]) * (
                    FRENQUENCE_FRANCAIS[lettre] - tableau_freq[lettre])
        else:
            distance += FRENQUENCE_FRANCAIS[lettre] * FRENQUENCE_FRANCAIS[
                lettre]
    distance = math.sqrt(distance)
    return distance

def calculer_PGCD(x :int, y :int) -> int:
    """fonction qui calcul le plus grand diviseur commun

    Args:
        x (int): un nombre
        y (int): un nombre

    Returns:
        int: le plus grand diviseur commun
    """
    gauche = x
    droite = y
    while droite != 0:
        gauche = gauche % droite
        gauche, droite = droite, gauche
    return gauche
    
def inverse_modulaire(nombre :int, modulo :int) -> int:
    """fonction qui retourne l'inverse modulaire d'un nombre à un modulo

    Args:
        nombre (int): un nombre
        modulo (int): le modulo

    Returns:
        int: l'inverse modulaire, si il est égale à -1 il n'existe pas d'inverse modulaire
    """
    res = -1
    if calculer_PGCD(nombre, modulo) == 1:
        res = 1
        while not (nombre * res) % modulo == 1:
            res += 1
    return res


def passe_francais(textetraduit : str, texte: str) -> str:
    """Remet la casse, les espaces et la ponctuation

    Args:
        textetraduit (str): la chaine de caractère traduite
        texte (str): le texte original

    Returns:
        str: le texte traduit avec la casse, les espaces et la ponctuation
    """
    res = ""
    cpt = 0
    for caractere in clean(texte,True,True,True):
        if ord(caractere) >= 65 and ord(caractere) <= 90:
            res += textetraduit[cpt].upper()
            cpt += 1
        elif ord(caractere) >= 97 and ord(caractere) <= 122:
            res += textetraduit[cpt].lower()
            cpt += 1
        else:
            res += caractere
    return res


def clean(s : str, keep_space : bool =False, keep_case : bool =False, keep_poncuation : bool = False) -> str:
    """Transforme une chaine en ascii, supprime la ponctuation
    et les blancs. Si le second argumement est faux, passe tout en
    majuscule.

    Args:
        message (str): la chaine a passer en nombre
        keep_space(bool) : si les espaces doivent être garder
        keep_casse(bool) : si la case doit être garder
        keep_poncuation(bool) : si la ponctuation doit être garder

    Returns:
        str: le message passer en majuscule et mit sous les autres conditions
    """
    accents = "àèìòùáéíóúýâêîôûãñõäëïöüÿåçðø"
    accents_trad = "aoiouaeiouyaeiouanoaeiouyacdo"
    accents = accents + accents.upper()
    accents_trad = accents_trad + accents_trad.upper()
    tr = str.maketrans(accents, accents_trad)
    s = s.translate(tr)

    lettres_doubles = ["æ", "Æ", "œ", "Œ", "ß"]
    lettres_doubles_trad = ["ae", "AE", "oe", "OE", "ss"]
    for i, j in zip(lettres_doubles, lettres_doubles_trad):
        s = s.replace(i, j)
    if not keep_poncuation:
        for p in string.punctuation + "«»":
            s = s.replace(p, "")

    if not keep_space:
        for p in string.whitespace:
            s = s.replace(p, "")

    if not keep_case:
        s = s.upper()

    return s

def decale(texte :str, nb_premier :int) -> str:
    """décale le texte avec a

    Args:
        texte (str): le texte à décaler
        nb_premier (int): le nombre à utliser

    Returns:
        str: le texte décaler
    """
    res = ''
    inverse_mod = inverse_modulaire(nb_premier,26)
    for car in texte:
        nb_lettre = ALPHABET.index(car)
        nb_lettre = (nb_lettre*inverse_mod)%26
        res += ALPHABET[nb_lettre]
    return res

def decode_affine(txt :str) -> str:
    """retourne le texte déchiffrer avec affine

    Args:
        txt (str): le texte à déchiffrer

    Returns:
        str: le texte déchiffrer
    """
    texte_clean = clean(txt)
    res = ''
    val = None
    for nb_premier in range(26):
        texte_decal = decale(texte_clean, nb_premier)
        decode_cesar = cesar.decodecesar(texte_decal)
        distance = distance_texte(decode_cesar)
        if val is None or distance < val:
            val = distance
            res = decode_cesar

    return passe_francais(res,txt) 
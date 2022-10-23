import math

frequence_français = {'A' : 7.636,
 'B' : 0.901,
 'C' : 3.260,
 'D' : 3.669,
 'E' : 14.715,
 'F' : 1.066,
 'G' : 0.866,
 'H' : 0.737,
 'I' : 7.529,
 'J' : 0.613,
 'K' : 0.074,
 'L' : 5.456,
 'M' : 2.968,
 'N' : 7.095,
 'O' : 5.796,
 'P' : 2.521,
 'Q' : 1.362,
 'R' : 6.693,
 'S' : 7.948,
 'T' : 7.244,
 'U' : 6.311,
 'V' : 1.838,
 'W' : 0.049,
 'X' : 0.427,
 'Y' : 0.128,
 'Z' : 0.326}

def cryptagecesar(texte : str,cle :int) -> str:
    """crypte le message avec la clé

    Args:
        texte (str): le texte à crypter
        cle (int): la cle pour crypter

    Returns:
        str: le texte crypter
    """
    phrasecrypte = ""
    for lettre in [ord(char.upper()) for char in texte]:
        if lettre >= 65 and lettre<=90:
            newlettre=lettre+cle
            if newlettre > 90:
                newlettre -= 26
            if newlettre < 65:
                newlettre += 26
            phrasecrypte += chr(newlettre)
        else:
            phrasecrypte += chr(lettre)
    return phrasecrypte

def clecesar(texte : str) -> int:
    """permet d'obtenir la clé pour un texte

    Args:
        texte (str): le texte ou il faut obtenir la cle

    Returns:
        int: la cle pour décrypter
    """
    valeurrapprochement = None
    cle = 0
    for cletest in range(26):
        textetrad = cryptagecesar(texte,cletest)
        frequencetraduit = tableau_frequence(textetrad)
        distance = 0
        for lettre in frequence_français:
            if lettre in frequencetraduit:
                distance += (frequence_français[lettre] - frequencetraduit[lettre]) * (frequence_français[lettre] - frequencetraduit[lettre])
            else:
                distance += frequence_français[lettre] * frequence_français[lettre]
        distance = math.sqrt(distance)
        if valeurrapprochement is None or valeurrapprochement > distance:
            valeurrapprochement = distance
            cle = cletest
    return cle

def decodecesar(texte :str) ->str:
    """décode cesar sans la clé

    Args:
        texte (str): le texte à déchiffrer

    Returns:
        str: le texte déchiffrer
    """
    return cryptagecesar(texte,clecesar(texte))

def tableau_frequence(texte : str) -> 'dict[str,int]':
    """donne le nombre d'apparation de chaque lettre du texte

    Args:
        texte (str): le texte

    Returns:
        dict[str,int]: le nombre d'apparition de chaque lettre dans le texte
    """
    res = {}
    nb_lettre = 0 
    for car in texte:
        car_maj = car.upper()
        if car_maj in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if car_maj not in res.keys():
                res[car_maj] = 0
            res[car_maj] += 1
            nb_lettre += 1
    for keys in res.keys():
        res[keys] = res[keys] / nb_lettre * 100
    return res

# print(cryptagecesar('Bonjour',10))
# print(clecesar("igoay paroay yaxtussk igkygx gshozokad rkgjkx vurozowak kyz jkzkxsotk g jkbktox joizgzkax. or kyz giiakorro kt zxousvnk jgty xusk ruxy jk rg ikrkhxgzout jky ravkxigrky."))
# print(decodecesar("igoay paroay yaxtussk igkygx gshozokad rkgjkx vurozowak kyz jkzkxsotk g jkbktox joizgzkax. or kyz giiakorro kt zxousvnk jgty xusk ruxy jk rg ikrkhxgzout jky ravkxigrky."))

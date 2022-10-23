import math
import string
from lettre import Lettre_mot
from cesar import decodecesar
from affinne import decode_affine

def construire_list_francais() -> Lettre_mot:
    """fonction qui retourne un dictionnaire sous forme d'arbre lexicographique

    Returns:
        Lettre_mot: l'arbre lexicographique
    """
    res = Lettre_mot(" ")
    fichier = open("french.txt","r")
    for ligne in fichier:
        res.ajoute_mot(ligne[:-1])
    return res

mot_francais = construire_list_francais()

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

def Ic(texte : str) -> int:
    """donne l'indice de coicidence d'un texte

    Args:
        texte (str): le texte

    Returns:
        int: l'indice de coicidence du texte
    """
    ic = 0
    tableau_freq = tableau_frequence(texte)
    for lettre in tableau_freq.keys():
        ic += (tableau_freq[lettre] * (tableau_freq[lettre]-1))
    return ic/(len(texte) * (len(texte) -1))

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

def longueurclev(message : str, sous_enesemble :int = 3) -> int:
    """Retourne la longeur probable de la clé

    Args:
        message (str): le texte
        sous_enesemble (int, optional): regarde les groupes par combien. Defaults to 3.

    Returns:
        int: la longeur probable de la clé
    """
    message_clean = clean(message)
    repetition = dict()
    for i in range(len(message_clean)-sous_enesemble+1):
        sousgroupe = message_clean[i:i+sous_enesemble]
        if sousgroupe not in repetition.keys():
            repetition[sousgroupe] = []
        repetition[sousgroupe].append(i)
    
    distances = []
    for sous_groupe in repetition.keys():
        liste_position = repetition[sous_groupe]
        if len(liste_position) > 1:
            for pos in range(len(liste_position)-1):
                distances.append(liste_position[pos+1] - liste_position[pos])
    longueur = 0
    if  len(distances) == 0:
        return None
    elif len(distances) == 1:
        return distances[0]
    else:
        longueur = calculer_PGCD(distances[1],distances[0])
        for distance in distances:
            longueur = calculer_PGCD(longueur, distance)
    
    if longueur >= 2:
        return longueur
    else:
        return longueurclev(message,sous_enesemble+1)

def inverse_matrice_mod_26(matrice:'list[int,int,int,int]') ->'list[int,int,int,int]':
    """inverse la matrice sur le modulo 26

    Args:
        matrice (list[int,int,int,int]): la matrice

    Returns:
        list[int,int,int,int]: la matrice inverse
    """
    res = []
    det = matrice[0] * matrice[3] - matrice[1] * matrice[2]
    inverse_det = inverse_modulaire(det,26)
    if inverse_det == -1:
        return None
    coeff_d = matrice[3] * inverse_det
    while coeff_d < 0:
        coeff_d += 26
    while coeff_d >= 26:
        coeff_d -= 26
    res.append(coeff_d)
    coeff_b = (- matrice[1]) * inverse_det
    while coeff_b < 0:
        coeff_b += 26
    while coeff_b >= 26:
        coeff_b -= 26
    res.append(coeff_b)
    coeff_c = (- matrice[2]) * inverse_det
    while coeff_c < 0:
        coeff_c += 26
    while coeff_c >= 26:
        coeff_c -= 26
    res.append(coeff_c)
    coeff_a = matrice[0] * inverse_det
    while coeff_a < 0:
        coeff_a += 26
    while coeff_a >= 26:
        coeff_a -= 26
    res.append(coeff_a)
    return res

def distance_texte(texte : str) -> int:
    """donne la distance du texte par rapport au fréquence habituel du français

    Args:
        texte (str): le texte

    Returns:
        int: le distance du texte
    """
    tableau_freq = [nombre * 100 for nombre in tableau_frequence(texte)]
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

def decode_HILL(texte :str) -> str:
    """ decode un texte crypté par HILL

    Args:
        texte (str): le texte à décrypter

    Returns:
        str: le texte décrypter
    """
    matrice = []
    valeur = None
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    if a*d - c*b != 0 or (inverse_matrice_mod_26([a, b, c, d]) is not None):
                        texte_traduit = decode_avec_matrice(texte, [a, b, c, d])
                        if texte_traduit is not None:
                            if est_francais(texte_traduit, texte):
                                distance = distance_texte(texte_traduit)
                                if valeur is None:
                                    valeur = distance
                                    matrice = [a,b,c,d]
                                elif distance < valeur:
                                    valeur = distance
                                    matrice = [a,b,c,d]
    return passe_francais(decode_avec_matrice(texte, matrice),texte)

def decoupe_phrase(texte: str) -> 'list[str]':
    """retourne les mots d'une phrase

    Args:
        texte (str): le texte

    Returns:
        list[str]: les mots de la phrase
    """
    texte_pre_decoupe = clean(texte,True,True,False)
    res = texte_pre_decoupe.split()
    return res

def est_francais_simple(texte_traduituit : str) -> bool:
    """indique si le texte est français

    Args:
        texte_traduituit (str): le texte

    Returns:
        bool: si le texte est français
    """
    texte_francais = decoupe_phrase(texte_traduituit.lower())
    nombre_mot_francais = 0
    for mot in texte_francais:
        if mot_francais.est_contenu(mot):
            nombre_mot_francais += 1
    return nombre_mot_francais/len(texte_francais) > 0.7

def est_francais(texte_traduituit : str,texte :str) -> bool:
    """indique si le texte est français

    Args:
        texte_traduituit (str): le texte
        texte (str): la version original pour avoir les espaces

    Returns:
        bool: si le texte est français
    """
    texte_francais = decoupe_phrase(passe_francais(texte_traduituit,texte).lower())
    nombre_mot_francais = 0
    for mot in texte_francais:
        if mot_francais.est_contenu(mot):
            nombre_mot_francais += 1
    return nombre_mot_francais/len(texte_francais) > 0.7

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

def decoupe_bloc_en_deux(texte :str) -> 'list[(str,str)]':
    """découpe les lettres du texte par bloc de deux

    Args:
        texte (str): le texte

    Returns:
        list[(str,str)]: les lettres du texte par bloc de deux
    """
    res = []
    cpt = 0
    block = []
    for i in [ord(car) for car in clean(texte)]:
        lettre = i - 65
        block.append(lettre)
        cpt += 1
        if cpt == 2:
            cpt = 0
            res.append(block)
            block = []
    if cpt == 1:
        block.append(0)
        res.append(block)
    return res

def decode_avec_matrice(texte : str, matrice : 'list[int,int,int]') -> str:
    """decode un texte avec la matrice donné en entré

    Args:
        texte (str): le texte
        matrice (list[int,int,int]): la matrice

    Returns:
        str: le texte décodé avec la matrice
    """
    res = ""
    inverse_matrice = inverse_matrice_mod_26(matrice)
    if inverse_matrice is None:
        return None
    liste_block = decoupe_bloc_en_deux(texte)
    for block in liste_block:
        res += chr(((block[0] * inverse_matrice[0] + block[1] * inverse_matrice[1])%26+65))
        res += chr(((block[0] * inverse_matrice[2] + block[1] * inverse_matrice[3])%26+65))
    return res

def puissance(nombre :int, puissance :int) -> int:
    """fonction qui retourne le nombre à la puissance

    Args:
        nombre (int): un nombre 
        puissance (int): la puissance à apliquer

    Returns:
        int: le nombre à la puissance 
    """
    if puissance == 0:
        resultat = 0
    else:
        resultat = nombre
    for _ in range(1,puissance):
        resultat = resultat * nombre
    return resultat

def division_en_base(nombre : int, base : int) -> 'list[int]':
    """passe un nombre en puissance dans la base donner

    Args:
        nombre (int): le nombre
        base (int): la base à utiliser

    Returns:
        list[int]: la liste des valeurs par puissance du nombre dans la base 
    """
    res = []
    puissance_modulo = 0
    restant_nombre = nombre
    while puissance(base,puissance_modulo) < nombre:
        puissance_modulo += 1
    while puissance_modulo > 0:
        base_puissance = puissance(base,puissance_modulo)
        nombre_puissance = restant_nombre // base_puissance
        restant_nombre = restant_nombre - nombre_puissance * base_puissance
        res.insert(0,nombre_puissance)
        puissance_modulo -= 1
    res.insert(0,restant_nombre)
    return res

def decryptage_vignere_sans_cle(texte : str) -> str:
    """décrypte un texte crypté avec vignère

    Args:
        texte (str): le texte

    Returns:
        str: le texte décrypté
    """
    long = longueurclev(texte)
    cpt = 0
    phrasedecrypte = ""
    valeurrapprochement = None
    for i in range(puissance(26, long)):
        texte_traduit = ""
        division_i = division_en_base(i, 26)
        valeur = []
        for for_val in range(long):
            if for_val < len(division_i):
                valeur.append(division_i[for_val])
            else:
                valeur.append(0)
        for lettre in [ord(char.upper()) for char in texte]:
            if lettre >= 65 and lettre<=90:
                newlettre = lettre - valeur[len(valeur)- cpt -1]
                while newlettre > 90:
                    newlettre -= 26
                while newlettre < 65:
                    newlettre += 26
                texte_traduit += chr(newlettre)
                cpt += 1
                if cpt == long:
                    cpt = 0
            else:
                texte_traduit += chr(lettre)
        frequencetraduit = tableau_frequence(texte_traduit)
        distance = distance_texte(texte_traduit)
        if valeurrapprochement is None or distance < valeurrapprochement:
            if est_francais(texte_traduit):
                valeurrapprochement = distance
                phrasedecrypte = texte_traduit
    return phrasedecrypte

def auto_decode(texte : str) -> str:
    """fonction qui décode un texte si il a été codé avec
    cesar, affinne, Hill ou vignere

    Args:
        texte (str): le texte à décrypter

    Returns:
        str: le texte décrypter
    """
    if Ic(texte) > 0.04:
        texte_ceasar = decodecesar(texte)
        if est_francais_simple(texte_ceasar):
            return passe_francais(clean(texte_ceasar),texte)
        else:
            texte_affinne = decode_affine(texte)
            if est_francais_simple(texte_affinne):
                return texte_affinne
            else:
                return "subsitution"
    else:
        if longueurclev(texte) == 2:
            return "decode_HILL(texte)"
        else:
            return "decryptage_vignere_sans_cle(texte)"
        

print(auto_decode("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."))
print(auto_decode("Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."))
print(auto_decode("Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."))
print(auto_decode("Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj. Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."))
print(auto_decode("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb."))

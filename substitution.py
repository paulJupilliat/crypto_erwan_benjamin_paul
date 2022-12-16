import string
from lettre import Lettre_mot
from itertools import combinations

ALPHABET_FRANCAIS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def construire_list_francais() -> Lettre_mot:
    """fonction qui retourne un dictionnaire sous forme d'arbre lexicographique

    Returns:
        Lettre_mot: l'arbre lexicographique
    """
    res = Lettre_mot(" ")
    res.ajoute_mot("bonjour")
    # fichier = open("french.txt","r")
    # for ligne in fichier:
    #     res.ajoute_mot(ligne[:-1])
    return res

mot_francais = construire_list_francais()

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
 'Z' : 0.326
}

LISTE_ALPHABET_TRIE=[ ('E', 14.715),
('S', 7.948),
('A', 7.636),
('I', 7.529),
('T', 7.244),
('N', 7.095),
('R', 6.693),
('U', 6.311),
('O', 5.796),
('L', 5.456),
('D', 3.669),
('C', 3.26),
('M', 2.968),
('P', 2.521),
('V', 1.838),
('Q', 1.362),
('F', 1.066),
('B', 0.901),
('G', 0.866),
('H', 0.737),
('J', 0.613),
('X', 0.427),
('Z', 0.326),
('Y', 0.128),
('K', 0.074),
('W', 0.049)
]

def tableau_frequence(texte):
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

def encode_substitution(message, subsitution):
    messageclean = clean(message)
    coder = ""
    for lettre in messageclean:
        coder += subsitution[ALPHABET_FRANCAIS.find(lettre)]
    return passe_francais(coder,message)

def generer_combinaison():
    for i in range(1,26):
        matrice = ""
        matrice += ALPHABET_FRANCAIS[i]
        for j in range(1,26):
            if j==i:
                matrice += "A"
            else:
                matrice += ALPHABET_FRANCAIS[j]
        print(matrice)


def liste_par_frequence(tableau_frequence):
    dico = list(tableau_frequence.items())
    return sorted(dico, key=lambda lettre: lettre[1], reverse=True)

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

def decode_auto(message):
    frequence_lettre = liste_par_frequence(tableau_frequence(message))
    list_base = create_list(frequence_lettre)
    origine = "".join(list_base)
    for combinaison in combinations(LISTE_ALPHABET_TRIE,len(frequence_lettre)):
        cle = creer_cle(combinaison)
        traduit = encode_substitution_avec_origine(message,cle,origine,True)
        if est_francais_simple(traduit):
            return traduit
    return "Impossible"

def create_list(frequence_lettre):
    res = list()
    for frequence in frequence_lettre:
        res.append(frequence[0])
    return res

def creer_cle(list_nombre):
    res = ""
    for pos in list_nombre:
        res += pos[0]
    return res

def encode_substitution_avec_origine(message, subsitution, origine, encode):
    messageclean = clean(message)
    coder = ""
    for lettre in messageclean:
        if encode:
            coder += subsitution[origine.find(lettre)]
        else:
            coder += origine[subsitution.find(lettre)]
    return coder

coder = passe_francais(encode_substitution_avec_origine("BONJOUR SHERLOCK, comment allez-vous?","DABCFEHGJIMNKLOPQRSTUVWXYZ",ALPHABET_FRANCAIS,True),"BONJOUR SHERLOCK, comment allez-vous?")
decoder = encode_substitution_avec_origine(coder,"DABCFEHGJIMNKLOPQRSTUVWXYZ",ALPHABET_FRANCAIS,False)
coder2 = encode_substitution_avec_origine("bonjour","ABCDFEHGJIMNKLOPQRSTUVWXYZ",ALPHABET_FRANCAIS,True)
print(passe_francais(decoder,coder))
print(decode_auto(coder))
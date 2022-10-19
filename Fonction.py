import math
import string
from tokenize import String

def construire_list_francais():
    res = []
    fichier = open("french.txt","r")
    for ligne in fichier:
        res.append(ligne[:-1])
    return res

mot_francais = sorted(construire_list_francais())

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

def clean(s, keep_space=False, keep_case=False, keep_poncuation = False):
    """Transforme une chaine en ascii, supprime la ponctuation
    et les blancs. Si le second argumement est faux, passe tout en
    majuscule."""
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

def calculer_PGCD(x,y):
    gauche = x
    droite = y
    while droite != 0:
        gauche = gauche % droite
        gauche, droite = droite, gauche
    return gauche

def tableau_frequence(texte):
    res = {}
    for lettre in [ord(char.upper()) for char in clean(texte)]:
        if lettre >= 65 and lettre <= 90:
            if chr(lettre) not in res.keys():
                res[chr(lettre)] = 0
            res[chr(lettre)] += 1
    return res

def Ic(texte):
    ic = 0
    tableau_freq = tableau_frequence(texte)
    for lettre in tableau_freq.keys():
        ic += (tableau_freq[lettre] * (tableau_freq[lettre]-1))
    return ic/(len(texte) * (len(texte) -1))

def inverse_modulaire(nombre, mod):
    res = -1
    if calculer_PGCD(nombre, mod) == 1:
        res = 1
        while not (nombre * res) % mod == 1:
            res += 1
    return res

def inverse_matrice_mod_26(matrice:list[int,int,int,int]):
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

def distance_texte(texte):
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

def decode_HILL(texte):
    matrice = []
    valeur = None
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    if a*d - c*b != 0 or (inverse_matrice_mod_26([a, b, c, d]) is not None):
                        texte_traduit = decode_avec_matrice(texte, [a, b, c, d])
                        if texte_traduit is not None:
                            distance = distance_texte(texte_traduit)
                            if est_francais(texte_traduit, texte):
                                print(distance)
                                print(valeur)
                                if valeur is None:
                                    valeur = distance
                                    matrice = [a,b,c,d]
                                elif distance < valeur:
                                    valeur = distance
                                    matrice = [a,b,c,d]
    print(matrice)
    return passe_francais(decode_avec_matrice(texte, matrice),texte)

def decoupe_phrase(texte: str) -> list[str]:
    texte_pre_decoupe = clean(texte,True,True,False)
    res = texte_pre_decoupe.split()
    return res

def est_francais(textetraduit,texte):
    texte_francais = sorted(decoupe_phrase(passe_francais(textetraduit,texte).lower()))
    index_texte = 0
    index_mot = 0
    nombre_mot_francais = 0
    while index_texte < len(texte_francais) and index_mot < len(mot_francais):
        if texte_francais[index_texte] < mot_francais[index_mot]:
            index_texte += 1
        elif texte_francais[index_texte] > mot_francais[index_mot]:
            index_mot += 1
        else:
            index_texte += 1
            nombre_mot_francais += 1
    return nombre_mot_francais/len(texte_francais) > 0.7

def passe_francais(textetraduit, texte):
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

def decoupe_bloc_en_deux(texte):
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


def decode_avec_matrice(texte, matrice):
    res = ""
    inverse_matrice = inverse_matrice_mod_26(matrice)
    if inverse_matrice is None:
        return None
    liste_block = decoupe_bloc_en_deux(texte)
    for block in liste_block:
        res += chr(((block[0] * inverse_matrice[0] + block[1] * inverse_matrice[1])%26+65))
        res += chr(((block[0] * inverse_matrice[2] + block[1] * inverse_matrice[3])%26+65))
    return res

print(inverse_matrice_mod_26([2,3,1,5]))
# print(1)
# print(Ic("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."))
# print("mono")
# print(2)
# print(Ic("Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."))
# print("poly")
# print(3)
# print(Ic("Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."))
print(decode_HILL("Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."))
texte = "Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."
# print(passe_francais(decode_avec_matrice(texte,[2,3,1,5]),texte))
# print("poly")
# print(4)
# print(Ic("Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj. Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."))
# print("mono")
# print(5)
# print(Ic("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb."))
# print("mono")

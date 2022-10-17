from re import T
import string
import fichier1

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

def clean(s, keep_space=False, keep_case=False):
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

    for p in string.punctuation + "«»":
        s = s.replace(p, "")

    if not keep_space:
        for p in string.whitespace:
            s = s.replace(p, "")

    if not keep_case:
        s = s.upper()

    return s

def tableau_frequence(text):
        """
        fontion qui renvoi la frequence d'apparition des lettres dans un texte passé en parametre
        """
        texte = clean(text,False,False)
        freq = dict()
        for l in texte:
            if l in ALPHABET:
                if l in freq:
                    freq[l]+=1
                else:
                    freq[l]=1
        for lettre in ALPHABET:
            if lettre not in freq:
                freq[lettre] = 0
            else : 
                freq[lettre] = freq[lettre]/len(text)*100
        return freq
print(tableau_frequence(fichier1.message1))



# def tableau_frequence(texte):
#     res = {}
#     for lettre in [ord(char.upper()) for char in texte]:
#         if lettre >= 65 and lettre <= 90:
#             if lettre not in res.keys():
#                 res[lettre] = 0
#             res[lettre] += 1
#     return res

def Ic(texte):
    ic = 0
    tableau_freq = tableau_frequence(texte)
    for lettre in tableau_freq.keys():
        ic += (tableau_freq[lettre] * (tableau_freq[lettre]-1))
    return ic/(len(texte) * (len(texte) -1))

def inverse_matrice_mod_26(matrice:list[int,int,int,int]):
    res = []
    det = matrice[0] * matrice[3] - matrice[1] * matrice[2]
    coeff_d = matrice[3] * det
    while coeff_d < 0:
        coeff_d += 26
    while coeff_d >= 26:
        coeff_d -= 26
    res.append(coeff_d)
    coeff_c = (- matrice[2]) * det
    res.append(coeff_c)
    coeff_b = (- matrice[1]) * det
    res.append(coeff_b)
    coeff_a = matrice[0] * det
    res.append(coeff_a)

def decode_HILL(texte):
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a*d-c*b!=0:
                        inverse = inverse_matrice_mod_26([a,b,c,d])

print(1)
print(Ic("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."))
print("mono")
print(2)
print(Ic("Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."))
print("poly")
print(3)
print(Ic("Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."))
print("poly")
print(4)
print(Ic("Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj. Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."))
print("mono")
print(5)
print(Ic("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb."))
print("mono")


def decode_affine(texte):
    #on regarde la frequence la plus haute de notre texte = e français
    #on creer l'équation a deux inconnu 
    #on obtient pls resultat A= et B= 
    #on teste avec les autres lettre du texte 
    #on compare la vague de frequence avec celle du language francais 
    # on retourne le A et le b POUR LEQUEL LA DISTANCE EST LA MOINS GRANDE

    # max_frequence = max(tableau_frequence(texte), key = lambda item:item.values())
    texte = clean(texte)
    liste_lettre_freq = [(val, lettre)for lettre, val in tableau_frequence(texte).items()]
    
    print(liste_lettre_freq)
    lettre_plus_use = max(liste_lettre_freq)[1]
    print(lettre_plus_use)
    y = ALPHABET.index(lettre_plus_use)
    x = ALPHABET.index("E") #on dis alors que x est la valeur de e car c'est la lettre avec la frequence la plus haute dans un dico français 
    les_solutions = couple_solutions(y,x)
    for solu in range(len(les_solutions)):
        sol_freq = tableau_frequence(solu)
        distance = dist(sol_freq, FRENQUENCE_FRANCAIS) 
        distance_min = 0
        if distance_min == 0 or distance < distance_min:
            distance_min = distance
            couple = solu
    (A,B) = couple
    texte_decode = ''
    for lettre in texte:
        lettre_decode = ALPHABET.index(lettre)*A +B
        texte_decode += lettre_decode
    return texte_decode
    # for sol in range(len(les_solutions))
    # tableau de fraquence de la solution1
    # tableau de frequence de la solution 2
    # ...
    # 
    # for tab in tableau de frequence_solution
    # distance_min = 0
    # tableau 
    


def couple_solutions(y, x):
    """fonction retournant les différentes solutions différentes pour une équation avec B mod 26

    Args:
        y (int): une valeur %26
        x (int): une valeur %26

    Returns:
        list[tuple]:la liste des tuples A et B solution de l'équation 
    """
    A = 0
    B = 0
    resultats = [(0,y)]
    while B < 26:
        A += 1
        if A*x+B != y:
            B=0
            B+=1
        else:
            resultats.append(A,B)
    return resultats
        

def dist(dico1, dico2):
    """recherche la plujs petite distance entre deux dictionnaires

        Args:
            dico1 (dict): le premier dictionnaire
            dico2 (dict): le second dictionnaire
        Return:
            int: la distance la plus petite entre deux clé des dictionnaire
    """
    distance = None
    for lettre in dico1.keys():
        for lettre2 in dico2.keys():
            distance_test = abs(dico1[lettre] - dico2[lettre2])
            if distance is None or distance_test < distance:
                distance = distance_test
                lettres = (lettre, lettre2)
    return ALPHABET.index(lettres[0]) - ALPHABET.index(lettres[1])
    
    



decode_affine(fichier1.message1)
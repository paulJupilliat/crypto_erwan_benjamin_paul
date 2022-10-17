from math import sqrt
import string
from fichier1 import message1
alphabet = string.ascii_uppercase


fr_frequence = {"A":8.4,"B":1.06,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":8.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}


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
print(clean(message1, False, False))

#Nous regardons si la methode de cryptage est fréquentielle ou si cela n'a pas de sens.
def frequences(text):
        """
        fontion qui renvoi la frequence d'apparition des lettres dans un texte passé en parametre
        """
        texte = clean(text,False,False)
        freq = dict()
        for l in texte:
            if l in alphabet:
                if l in freq:
                    freq[l]+=1
                else:
                    freq[l]=1
        for lettre in alphabet:
            if lettre not in freq:
                freq[lettre] = 0
            else : 
                freq[lettre] = freq[lettre]/len(text)*100
        return freq
print(frequences(message1))





# grace à ces fonctions, nous trouvons que la lettre la plus utilisé dans le fichier 1 est le V :  9.3 suivi du H: 8.8 et du U : 8.5
# en comparant ces frequence avec les frenquences des lettres dans le langauge français, cela signifirait que V = E, A = H OU A=U 

def correspondance(dico_frequ_txt, dico_freq_fr):
    """Fait correspondre chaque lettre à une lettre de la langue française grâce à leur fréquence dans le texte par rapport à la langue fr

    Args:
        dico_frequ_txt (dict(str: float)): dictionnaire de fréquence d'apparition des lettres dans le texte
        dico_freq_fr (dict(str: float)): dictionnaire de fréquence d'apparition des lettres dans la langue fr
    """
    res = dict()
    for lettre in dico_frequ_txt:
        res[lettre] = plus_proche_freq(dico_frequ_txt[lettre], dico_freq_fr)
    return res

def plus_proche_freq(frequence, dico_freq_langue):
    min_trouve = None
    for lettre, freq_lettre in dico_freq_langue.items():
        if min_trouve is None or abs(frequence - freq_lettre) < min_trouve[1]:
            min_trouve = (lettre, abs(frequence - freq_lettre))
    return min_trouve[0]

print(correspondance(frequences(message1),fr_frequence))

# en comparant les lettres avec leur correspondance dans le dico des frequences, nous pouvons établir qu'il s'agit bel et bien d'un codage monoalphabetique car beacoup de lettre comme "VK" se situe souvent dans cette ordre en un seul mot. On suppose que chaque lettre codé a donc une seule lettre decodé
# Il ne s'agit pas du décryptage de cesar car un simple decalage ne permet de pas de décoder ce texte
# Nous suppossons qu'il s'agit alors d'un cryptage de type affine

    #on part du principe ou


def dechiffrementAffine(a,b,L):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    x=alphabet.index(L)
    y=(inverse(a)*(x-b))%26
    return alphabet[y]
    
print(dechiffrementAffine(4,2,"A"))

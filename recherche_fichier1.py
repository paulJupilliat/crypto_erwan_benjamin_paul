import string
from fichier1 import message1

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
#code et decode substitution

#on regarde toutes les possibilités et on affiche le message décoder, si ce message comporte les mot d'un dictionnaire français alors on la garde
#si on a pas de mot correspondant alors on passe a une autre possibilité
def plus_grand_mot(message):
    mot = ""
    mot_max = ""
    for lettre in message:
        if lettre != " ":
            mot += lettre
        else:
            mot += " "
            if len(mot)>len(mot_max) or mot_max == "":
                mot_max = mot
                mot = ""
    return mot_max

def creer_decallage(num):
    """fonction permettant de créer deux alphabets en fonction du decallage"""
    i=num
    alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet_2 = ""
    for lettre in range(len(alphabet_1)):
        if i < 26:
            alphabet_2 += alphabet_1[i]
            i += 1
        else:
            i =0
            alphabet_2 += alphabet_1[i]
            while i < num-1:
                i += 1
                alphabet_2 += alphabet_1[i]
            break
    return alphabet_2



def equivalence(alphabet_debut, alphabet_2, message):
    for lettre in message:
        if lettre in alphabet_debut:
            message = message.replace(lettre, alphabet_2[alphabet_debut.index(lettre)])
        if lettre in alphabet_2:
            message = message.replace(lettre, alphabet_debut[alphabet_2.index(lettre)])
    return message


def decode(message):
    mot_fr = open("crypto_erwan_benjamin_paul/fichier_test.txt","r")#open("crypto_erwan_benjamin_paul/french.txt", "r")
    lignes = mot_fr.readlines()
    print(lignes)
    alphabet_debut = "abcdefghijklmnopqrstuvwxyz"
    #tant que le message decaller n'est pas dans le dictionnaire francais, on decale d'encore 1
    #peut etre prendre le plus grand mot du message pour verifier dans le dico francais
    res = True
    while res:
        for i in range(26):
            alphabet_2 = creer_decallage(i)
            message = equivalence(alphabet_debut, alphabet_2, message)
            for element in lignes:
                if plus_grand_mot(message)  == element.strip()+"\n":
                    res = False
                    break
    return message



message = "YR CNYNVF QR CNHY" #le palais de paul



print(plus_grand_mot(message))

print(decode(message))


    



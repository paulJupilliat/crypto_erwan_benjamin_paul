#code et decode substitution

#on regarde toutes les possibilités et on affiche le message décoder, si ce message comporte les mot d'un dictionnaire français alors on la garde
#si on a pas de mot correspondant alors on passe a une autre possibilité


def creer_decallage(num):
    """fonction permettant de créer deux alphabets en fonction du decallage"""
    i=num
    alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
    print(alphabet_1)
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



message = "YR CNYNVF QR CNHY" #le palais de paul

print(creer_decallage(10))


    



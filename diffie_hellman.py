from math import sqrt
from random import randint
from Personne import Personne
from brut_force import baby_step_giant_step, test_brute_force


def est_premier(n):
    """Renvoie True si n est premier, False sinon
    Args:
        n (int): un entier
    Returns:
        bool: True si n est premier, False sinon
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

def genere_nombre_premier(max):
    """Génère un nombre premier inférieur à max
    Args:
        max (int): un entier
    Returns:
        int: un nombre premier inférieur à max
    """
    n = randint(2, max)
    while not est_premier(n):
        n = randint(2, max)
    return n

def diffie_hellman_generation_cle():
    """Algorithme de Diffie-Hellman
    Returns:
        Personne, Personne: les deux personnes
        Xa, Yb: les clés écchangées
    """
    # Initialisation des deux personnes
    personne1 = Personne()
    personne2 = Personne()

    # Génération de la clé publique
    p = genere_nombre_premier(1000)
    g = genere_nombre_premier(p-1)

    # On envoie la clé publique à chaque personne
    personne1.set_cle_publique((g, p))
    personne2.set_cle_publique((g, p))

    # Génère et échange les clés
    Ay = personne1.genere_echange()
    By = personne2.genere_echange()
    personne1.set_cle_partagee(By)
    personne2.set_cle_partagee(Ay)

    # Calcul de la clé partagée
    personne1.genere_cle()
    personne2.genere_cle()
    
    # retourne les personnes pour les utiliser 
    return personne1, personne2, Ay, By

if __name__ == "__main__":
    print("╒" + "═" * 50 + "╕")
    print("│" + " " * 15 + "Diffie Hellman" + " " * 15 + "│")
    print("╘" + "═" * 50 + "╛")
    print("│  1. Cas exemple" + " " * 35 + "│")
    print("│  2. Tester" + " " * 36 + "│")
    print("╘" + "═" * 50 + "╛")
    choix = input("Choix: ")
    if choix == "1":
        print("╒" + "═" * 50 + "╕")
        personne1, personne2, _, Bx = diffie_hellman_generation_cle()
        personne3, personne4, _, _ = diffie_hellman_generation_cle()
        message = "Bonjour ceci est un test de la crypto Diffie Hellman !"
        message_chiffre = personne1.envoie_message(message)
        print(f"La première personne envoie: {message_chiffre}")
        message_essaie_dechiffre = personne3.recoit_message(message_chiffre)
        message_dechiffre = personne2.recoit_message(message_chiffre)
        print(f"La deuxième personne la décrypte: {message_dechiffre}")
        print(f"La troisième personne essaie de décrypter: {message_essaie_dechiffre} \n \n")
        message_chiffre_2 = personne2.envoie_message("Oh le fameuse technique de Diffie Hellman, essaye de me décrypter !")
        message_dechiffre_2 = personne1.recoit_message(message_chiffre_2)
        print(f"La deuxième personne envoie: {message_chiffre_2}")
        print(f"La première personne la décrypte: {message_dechiffre_2}")
        print(f"La troisième personne essaie de décrypter: {personne3.recoit_message(message_chiffre_2)}")
        print(f"La troisième personne essaye de brut force car elle connait la longeur de la clé: {test_brute_force(personne1.get_cle_a_partage(), personne1.get_cle_publique()[1], personne1.get_cle_publique()[0])}")
        personne4.set_cle_publique(personne1.get_cle_publique())
        personne4.set_cle_prive(test_brute_force(personne1.get_cle_a_partage(
        ), personne1.get_cle_publique()[1], personne1.get_cle_publique()[0]))
        personne4.set_cle_partagee(Bx)
        personne4.genere_cle()
        print(personne4.recoit_message(message_chiffre_2))
        # saut de ligne
        print(" ")
        print("╒" + "═" * 16 + "baby step big step" + "═" * 16 + "╕")
        print(f"|     Deuxieme encrytion" + " " * 27 + f"|")
        personne1v2, personne2v2, _, _ = diffie_hellman_generation_cle()
        personne1v2.envoie_message(message_chiffre)
        print(f"|     Après la deuxième encryption le message envoyé est:")
        print(f"|     baby {baby_step_giant_step(personne1v2.get_cle_publique()[0], personne1v2.get_cle_publique()[1], personne1.get_cle_a_partage())}")

        print("╘" + "═" * 50 + "╛")
    elif choix == "2":
        personne1, personne2, _, _ = diffie_hellman_generation_cle()
        message = input("Message à envoyer: ")
        message_chiffre = personne1.envoie_message(message)
        print(f"La première personne envoie: {message_chiffre}")
        message_dechiffre = personne2.recoit_message(message_chiffre)
        print(f"La deuxième personne la décrypte: {message_dechiffre}")

        print("╒" + "═" * 50 + "╕")
        print("│ 1. Brut force" + " " * 36 + "│")
        print("│ 2. Quitter" + " " * 37 + "│")
        print("╘" + "═" * 50 + "╛")
        choix = input("Choix: ")
        if choix == "1":
            print(
                f"La troisième personne essaye de brut force car elle connait la longeur de la clé: {test_brute_force(personne1.get_cle_a_partage(), personne1.get_cle_publique()[1], personne1.get_cle_publique()[0])}")
        elif choix == "2":
            exit()
        else:
            print("Choix invalide")

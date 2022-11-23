"""Contient le main pour décrypter les fichiers textes du défi 1 de la sae crypto """
from fonction import auto_decode
from textes import *

def main():
    """Main du programme"""
    continu = True
    while continu:
        print("╔════════════════════════════════╗")
        print("║         Menu du défi 1         ║")
        print("╚════════════════════════════════╝")
        print("║ Choisir un texte à décrypter : ║")
        print("║ 1. TEXTE1                      ║")
        print("║ 2. TEXTE2                      ║")
        print("║ 3. TEXTE3                      ║")
        print("║ 4. TEXTE4                      ║")
        print("║ 5. TEXTE5                      ║")
        print("║ 6. Quitter                     ║")
        print("╚════════════════════════════════╝")
        choix = input("▐          Votre choix :         ▐" + "\n")
        if choix == "1":
            print("╔════════════════════════════════╗")
            print("║" + TEXTE1 )
            print("╚--------------------------------╝")
            print("║   Résultat décrypté(en cours): ║")
            print("║    " + auto_decode(TEXTE1)[0])
            print("║" + auto_decode(TEXTE1)[1]) 
            print("╚════════════════════════════════╝")
        elif choix == "2":
            print("╔════════════════════════════════╗")
            print("║" + TEXTE2 )
            print("╚--------------------------------╝")
            print("║   Résultat décrypté(en cours): ║")
            print("║" + auto_decode(TEXTE2)[0])
            print("║" + auto_decode(TEXTE2)[1])
            print("╚════════════════════════════════╝")
        elif choix == "3":
            print("╔════════════════════════════════╗")
            print("║" + TEXTE3 )
            print("╚--------------------------------╝")
            print("║   Résultat décrypté(en cours): ║")
            print("║" + auto_decode(TEXTE3)[0])
            print("║" + auto_decode(TEXTE3)[1])
            print("╚════════════════════════════════╝")
        elif choix == "4":
            print("╔════════════════════════════════╗")
            print("║" + TEXTE4 )
            print("╚--------------------------------╝")
            print("║   Résultat décrypté(en cours): ║")
            print("║" + auto_decode(TEXTE4)[0])
            print("║" + auto_decode(TEXTE4)[1])
            print("╚════════════════════════════════╝")
        elif choix == "5":
            print("╔════════════════════════════════╗")
            print("║" + TEXTE5 )
            print("╚--------------------------------╝")
            print("║   Résultat décrypté(en cours): ║")
            print("║" + auto_decode(TEXTE5)[0])
            print("║" + auto_decode(TEXTE5)[1])
            print("╚════════════════════════════════╝")
        elif choix == "6":
            continu = False
        else:
            print("╔════════════════════════════════╗")
            print("║   Veuillez entrer un nombre    ║")
            print("║   entre 1 et 5.                ║")
            print("╚════════════════════════════════╝")
        print("║ Appuyez sur entrée pour        ║")
        print("║ continuer.                     ║")
        print("╚════════════════════════════════╝")
        input()

main()


from random import randint

class Personne:
    def __init__(self):
        self.__cle_prive = randint(1, 1000)
        self.cle_publique = None # (g, p)
        self.cle_partagee = None #Clé reçue par l'autre personne
        self.__cle = None #Clé calculée
    
    def set_cle_publique(self, cle_publique: tuple[int, int]) -> None:
        """Set la clé publique

        Args:
            cle_publique (int, int): la clé publique
        """
        self.cle_publique = cle_publique
    
    def set_cle_partagee(self, cle_partagee: int) -> None:
        """Set la clé qui à été envoyé par l'autre personne

        Args:
            cle_partagee (int): la clé partagée
        """
        self.cle_partagee = cle_partagee

    def genere_echange(self) -> int:
        """Génère un int à envoyer à l'autre personne
        Returns:
            int: le int à envoyer à l'autre personne
        """
        return self.cle_publique[0]**self.__cle_prive % self.cle_publique[1]

    def genere_cle(self) -> int:
        """Génère la clé partagée
        """
        self.__cle = self.cle_partagee**self.__cle_prive % self.cle_publique[1]

    def get_cle(self) -> int:
        """Renvoie la clé partagée
        Returns:
            int: la clé partagée
        """
        return self.__cle

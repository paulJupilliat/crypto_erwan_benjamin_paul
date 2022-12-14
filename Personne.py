import math
from random import randint


class Personne:
    def __init__(self):
        self.__cle_prive = randint(1, 1000)
        self.cle_publique = None  # (g, p)
        self.cle_a_partagee = None #Clé a partager à l'autre user
        self.cle_partagee = None  # Clé reçue par l'autre personne
        self.__cle = None  # Clé calculée

    def set_cle_publique(self, cle_publique: tuple[int, int]) -> None:
        """Set la clé publique

        Args:
            cle_publique (int, int): la clé publique
        """
        self.cle_publique = cle_publique

    def set_cle_prive(self, cle_privee: int) -> None:
        """Set la clé privee

        Args:
            cle_publique (int, int): la clé publique
        """
        self.__cle_prive = cle_privee

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
        self.cle_a_partagee = (self.cle_publique[0]**self.__cle_prive) % self.cle_publique[1]
        return self.cle_a_partagee

    def genere_cle(self) -> int:
        """Génère la clé partagée
        """
        self.__cle = (self.cle_partagee**self.__cle_prive) % self.cle_publique[1]

    def get_cle(self) -> int:
        """Renvoie la clé partagée par l'autre personne
        Returns:
            int: la clé partagée
        """
        return self.__cle

    def envoie_message(self, message: str) -> str:
        """Envoie un message à l'autre personne en le chiffrant
        Args:
            message (str): le message à envoyer
        Returns:
            str: le message chiffré
        """
        message_chiffre = ""
        for lettre in message:
            message_chiffre += chr((ord(lettre) * self.__cle) % 1114112)
        return message_chiffre

    def recoit_message(self, message: str) -> str:
        """Reçoit un message chiffré avec diffie Helman

        Args:
            message (str): Le message reçu

        Returns:
            str: Le message décodé
        """
        message_decode = ""
        for lettre in message:
            ind_lettre = (ord(lettre) // self.__cle)
            message_decode += chr(ind_lettre)
        return message_decode

    def len_cle(self) -> int:
        """Renvoie la longueur de la clé
        Returns:
            int: la longueur de la clé
        """
        return len(str(self.__cle))
    
    def len_cle_pvr(self) -> int:
        """Renvoie la longueur de la clé secrète
        Retruns:
            int: la longueure de la clé secrète
        """
        return len(str(self.__cle_prive))

    def get_cle_publique(self) ->tuple[int, int]:
        """Renvoie la clé publique
        Return:
            int, int: q, p
        """
        return (self.cle_publique[0], self.cle_publique[1])
    
    def get_cle_pvr(self):
        """Renvoie la clé secrète de la personne
        Returns:
            int: la clé secrète de la personne
        """
        return self.__cle_prive

    def get_cle_a_partage(self) -> int:
        """Renvoir la clé que la personne doit partager
        Returns:
            int : La clé à partager
        """
        return self.cle_a_partagee

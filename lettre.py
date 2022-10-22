class Lettre_mot:
    """classe qui gére la recherche lexicographique
    """

    def __init__(self, lettre):
        self._lettre = lettre
        self._enfant = dict()

    def ajoute_mot(self, mot : str):
        """ajoute un mot à ses enfants

        Args:
            mot (str): le mot à ajouter
        """
        if len(mot) == 0:
            if " " not in self._enfant.keys():
                self._enfant[" "] = Lettre_mot(" ")
        else:
            if mot[0] not in self._enfant.keys():
                self._enfant[mot[0]] = Lettre_mot(mot[0])
            self._enfant[mot[0]].ajoute_mot(mot[1:])

    def est_contenu(self, mot : str) -> bool:
        """indique si le mot est contenue dans ses enfants

        Returns:
            bool: si le mot est présent
        """
        if len(mot) == 0:
            if " " in self._enfant.keys():
                return True
            else:
                return False
        else:
            if mot[0] in self._enfant.keys():
                return self._enfant[mot[0]].est_contenu(mot[1:])
            else:
                return False
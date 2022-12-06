from ..diffie_hellman import *
def test_est_premier():
    assert est_premier(2) == True
    assert est_premier(3) == True
    assert est_premier(4) == False
    assert est_premier(5) == True
    assert est_premier(5407) == True

def test_genere_nombre_premier():
    nombres = [genere_nombre_premier(100) for _ in range(100)]
    for n in nombres:
        assert est_premier(n) == True

def test_diffie_hellman():
    personne1, personne2 = diffie_hellman()
    assert personne1.get_cle() == personne2.get_cle()

def test_personne_set_cle_publique():
    personne = Personne()
    personne.set_cle_publique((2, 3))
    assert personne.cle_publique == (2, 3)

    personne.set_cle_publique(None)
    assert personne.cle_publique == None

def test_personne_set_cle_partagee():
    personne = Personne()
    personne.set_cle_partagee(2)
    assert personne.cle_partagee == 2

    personne.set_cle_partagee(None)
    assert personne.cle_partagee == None

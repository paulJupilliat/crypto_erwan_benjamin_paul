# Réponses

## Sommaire
- [Réponses](#réponses)
  - [Sommaire](#sommaire)
  - [Ex1](#ex1)
    - [Algo Diffie-Hellman](#algo-diffie-hellman)

## Ex1
1) Nous allons détailler le protocole Diffie-Hellman. 
Il permet d'échanger un clé secrète entre deux personnes sans avoir au préalable de secret en commun.
Il repose sur le logarithme discret.  
### Algo Diffie-Hellman
----

Pers1 et Pers2 génèrent ensemble deux nombres:  
- <span style="color: red">p</span> (un nombre premier)  
- <span style="color: red">g</span> (un nombre aléatoire > p)  

-----

Pers1 choisit un nombre <span style="color: red">a</span> (aléatoire) et calcule <span style="color: red">g<sup>a</sup> mod p</span>. Ce qui donne <span style="color: red">Ax</span>.  
Pers2 choisit un nombre <span style="color: red">b</span> (aléatoire) et calcule <span style="color: red">g<sup>b</sup> mod p</span>. Ce qui donne <span style="color: red">By</span>.

-----

Ils échangent alors leurs résultats respectifs.

-----

Pers1 calcule la clé secrète <span style="color: red">s</span>:   
    s = <span style="color: red">By<sup>a</sup> mod p</span>  
Ce qui est égale à <span style="color: red">(g<sup>a</sup><sup>b</sup>) mod p</span>  

------

Pers2 calcule la clé secrète <span style="color: red">s</span>:  
    s = <span style="color: red">Ax<sup>b</sup> mod p</span> 
<span style="color: red">(g<sup>a</sup><sup>b</sup>) mod p</span>  
Ce qui est égale à <span style="color: red">(g<sup>a</sup><sup>b</sup>) mod p</span>

-----
Ce protoole est vulnérable à une attaque sandwitch.  
    Une personne intersepte le message de Pers1 calcul un By et l'envoie à Pers1 (il se fait passer pour Pers2).
    Puis il envoie  le message de Pers1 à Pers2 (il se fait passer pour Pers1).
    Ils pensent passer directement l'un à l'autre mais en réalité ils passent par l'intermédiaire.

    
# Réponses

## Sommaire
- [Réponses](#réponses)
  - [Sommaire](#sommaire)
  - [Algorithme discret](#algorithme-discret)
    - [Définition](#définition)
  - [Ex1](#ex1)
    - [Algo Diffie-Hellman](#algo-diffie-hellman)
    - [Vulnérabilité](#vulnérabilité)
      - [Man in the middle](#man-in-the-middle)
      - [Meet in the middle](#meet-in-the-middle)
        - [Baby step giant step](#baby-step-giant-step)
          - [Algorithme](#algorithme)

## Algorithme discret
### Définition
G un groupe cyclique d'ordre *n* engendré par *g*. Tous *x* ∈ G peut s'écrire:
    <span style="color: red"> x = g<sup>α</sup>
    avec 0 ≤ α < *n*
    <span style="color: red">α</span> noté <span style="color: red"> log<sub>g</sub>(x)</span> est le log discret de *x* en base *g*

Si G est un groupe de point appartenant à une courbe élliptique(courbe non singulière), sur un corp fini, le meilleur algorithme pour calculer le logarythme discret 
est le pgcd étendu.

En résumé le logarythme discret permet de retrouver x dans une équation du type:  
    <span style="color: red"> a<sup>x</sup> = b mod p</span>
    

Il est la base de tous les moyens de cryptage à clé publique aujourd'hui utilisé. 

## Ex1
1) Nous allons détailler le protocole Diffie-Hellman. 
Il permet d'échanger un clé secrète entre deux personnes sans avoir au préalable de secret en commun.
Il repose sur le logarithme discret.  
### Algo Diffie-Hellman
----

Pers1 et Pers2 génèrent ensemble deux nombres:  
- <span style="color: red">p</span> (un nombre premier)  
- <span style="color: red">g</span> (un nombre aléatoire < p)  

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

------

<img src="../img/schema diffie"/>

-----
### Vulnérabilité
#### Man in the middle
Ce protoole est vulnérable à une attaque man in the middle.  
    Une personne intersepte le message de Pers1 calcul un By et l'envoie à Pers1 (il se fait passer pour Pers2).  
    Puis il envoie  le message de Pers1 à Pers2 (il se fait passer pour Pers1).   
    Ils pensent passer directement l'un à l'autre mais en réalité ils passent par l'intermédiaire.   

-----
Comme le logarithme discret est difficile à calculer, il est impossible de retrouver <span style="color: red">a</span> ou <span style="color: red">b</span> à partir de <span style="color: red">Ax</span> ou <span style="color: red">By</span>.

Il partage le problème du logarythme discret:   
si on a la valeur de g, p et g<sup>a mod p</sup> on ne peut pas trouver la valeur de a

------

#### Meet in the middle
<img src="img/../../img/schema%20meet%20in%20the%20middle.png">
Meet int the middle est une attaque qui consiste à chercher les deux clés secrètes en même temps.   
Deux tableau sont construit: 
- un avec le calcul avec la clé secrète de Pers1
- un avec le calcul avec la clé secrète de Pers2 
Une fois ces deux tableaux construit, on cherche l'intersection et on trouve la clé secrète.

-------

##### Baby step giant step
###### Algorithme
<img src="img/../../img/algo%20baby%20s.png">
Cette attaque est un algorithme de meet in the middle.

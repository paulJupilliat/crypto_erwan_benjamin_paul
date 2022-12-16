<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">crypto_erwan_benjamin_paul
</h3>

---

<p align="center"> Rendu du défi de la sae crypto
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [Rapport ](#rapport-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
- [🎈 Plus d'informations sur la méthodologie ](#-plus-dinformations-sur-la-méthodologie-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>
Rendu du défi 1 de la sae crypto de l'iut d'Orléans. Il permet de décypter des messages codé avec des anciennes méthodes

## Rapport <a name = "rapport"></a>
[Cliquez ici](./doc/Rapport.md)

## 🏁 Getting Started <a name = "getting_started"></a>

Pour tester le décryptages des textes, il faut lancer le fichier main.py avec python et suivre les instruction écrite dans le terminal.
ATTENTION: Certains décryptage peuvent prendre du temps.

Pour tester diffie-hellman, il faut lancer le fichier diffie_hellman.py avec python et suivre les instruction écrite dans le terminal.

### Prerequisites

pip install math

## 🎈 Plus d'informations sur la méthodologie <a name="usage"></a>

Nous disposons des échanges textuels codés par l’empire de Kaota.
Nous n’avons donc pas d’idée sur le type de cryptage utilisé, nous allons devoir étudier les fichiers afin de savoir quel type de cryptage est utilisé avant de le décrypter.

Pour décoder un texte automatiquement, nous cherchons l’indice de coïncidence pour déterminer le nombre d’alphabet utilisé (si c’est un cryptage mono ou poly alphabétique).
Nous obtenons des valeurs entre 0.4 et 0.5 sur certains texte, nous en déduisons qu’il s’agit d’un cryptage mono alphabétique. Dans ce cas, le codage a été fait avec : césar ou affine ou substitution.  
Pour découvrir avec quel codage cela a été fait, nous allons essayé de décoder le texte avec cesar puis utiliser la fonction  `est_français()` pour voir si le texte est a plus de 70% en français. Si ce n’est pas le cas, nous essayons avec affine et enfin avec la substitution.

Pour les autres textes nous obtenons des valeurs entre 0.2 et 0.3, ce qui correspond à un alphabet polyalphabétique. Le codage a été fait avec:  Hill ou vignère.  
Pour découvrir avec quel codage cela a été fait, nous allons estimer la longeur probable de la clé avec la fonction `longuerclev()`. Si la longueur est égale à 2, le codage est alors fait avec Hill. Sinon, il s’agit d’un codage vignère.  

Une fois que nous connaissons avec quel codage le texte a été codé, nous pouvons décoder le texte avec la fonction adapté.   
Pour chaque décodage, nous implémentons des théorèmes mathématiques vue en cours ou en TD ou sur internet.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org) - dev

## ✍️ Authors <a name = "authors"></a>

- [Depot git](https://github.com/BenGuerre/crypto_erwan_benjamin_paul) - Depot github du projet

Projet fait par le groupe Erwan MANACH, Benjamin GUERRE et Paul JUPILLIAT

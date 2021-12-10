# DM de Graphe 2021-2022

- [Le sujet 2021](https://www.fil.univ-lille1.fr/~varre/portail/graphes/dm/dm-21-22.pdf)
- [Rapport-KARFA-RACHMAT.pdf](Rapport-KARFA-RACHMAT.pdf)

toute notre réponse concernant le DM est dans notre dossier de rapport.

# Equipe

Ce travail est à réaliser en équipe dont les membres sont (**groupe 7 du S5 Licence 3 Informatique**) :

- BENEDICTUS KENT **RACHMAT**
- HICHEM **KARFA**

# Arborescence du projet

```bash
.
├── Makefile
├── README.md
├── Rapport-KARFA-RACHMAT.docx
├── Rapport-KARFA-RACHMAT.pdf
└── code
    ├── carte.py
    ├── carte_data.txt
    ├── gsm.py
    ├── gsm_data.txt
    ├── sudoku.py
    └── sudoku_data.txt

1 directory, 10 files
```

# Organisation du fichier

Le DM se répartir de la façon suivante :

- Le fichier `Makefile` : notre commande Makefile pour exécuter le code.
- Le fichier `Rapport-KARFA-RACHMAT.pdf` : notre compte rendu de ce DM ([lien](Rapport-KARFA-RACHMAT.pdf)).
- Le dossier `code/` : les algorithmes en python et les données nécessaires pour résoudre les questions.

# Exécution du projet

placez vous dans la racine et puis exécuter ce commande:

```bash
Pour le sujet de Sudoku
$ > make sudoku

Pour le sujet de Cartes Géographiques
$ > make carte

Pour le sujet de Allocation de fréquences dans les réseaux GSM
$ > make gsm
```

Pour nettoyer les réponses du graphe sauvegardée en `.txt`, exécutez la commande ci-dessous :

```bash
$ > make clean
```

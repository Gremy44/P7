# P7 -Résolvez des problèmes en utilisant des algorithmes en Python

## Sommaire

 - Installation
 - Utilisation
 - Flake8
## Installation
-   Cloner le git
    `git clone https://github.com/Gremy44/P7.git`
-   Créer votre environnement virtuel
`python -m venv env`
-   Activer l'environnement virtuel
`env/Scripts/activate`
-   Installer les librairies grâce au fichier 'requirements.txt'
`pip install -r requirements.txt`
-   Lire la rubrique 'Utilisation' pour utiliser les algorithmes
 ## Utilisation

Pour visualiser les résultats d'un jeu de données avec l'algorithme désiré :

    python <nom du script.py> <chemin relatif du jeu de donées>
ex :

    python brutforce.py data\1-Brut_force\data_brut_force.csv
    python optimized.py data\2-Optimise\dataset1_Python+P7.csv
    python optimized.py data\2-Optimise\dataset2_Python+P7.csv

> Attention : la solution de brut force fonctionne bien avec le jeu de
> données "data_brut_force" car celle-ci ne contient que peu de valeurs.
> L'algorithme de brut force fonctionnant par récursion, il risque
> d'être très gourmand en ressource s'il est utilisé avec le dataset 1
> ou 2.

## Flake8
Pour générer un rapport flake8 et vérifier que le code est bien écrit :
    `flake8 --format=html --htmldir=flake-report`
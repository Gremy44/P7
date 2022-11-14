# P7 -Résolvez des problèmes en utilisant des algorithmes en Python

## Sommaire

 - Installation
 - Utilisation
 ## Installation
 -   Cloner le git
-   Créer votre environnement virtuel
-   Installer les librairies grâce au fichier 'requirements.txt'
-   Lancer l'application
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
> d'être très gourmand en ressource s'il est utilisé avec le dataset_1
> ou 2.
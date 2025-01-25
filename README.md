# 3D Teeth Classification

Ce projet est une application de classification et de visualisation 3D de modèles de dents. Elle permet de classifier un modèle de dent en 7 catégories différentes à l'aide d'un modèle de réseau de neurones convolutif (CNN). L'application permet également aux utilisateurs de visualiser le modèle 3D de la dent téléchargée et d'explorer une vue à 360 degrés.

## Fonctionnalités

- **Classification de dents 3D** : Chargez un fichier `.obj` de dent 3D, et l'application classifie le modèle parmi les catégories suivantes : Canine, Deuxième molaire, Deuxième prémolaire, Incisive centrale, Incisive latérale, Première molaire, Première prémolaire.
- **Visualisation 3D** : Affichez et explorez un modèle 3D de la dent téléchargée.
- **Vues de dents à 360 degrés** : Permet aux utilisateurs de visualiser le modèle sous tous les angles en faisant pivoter l'image à l'aide de la souris.

## Prérequis

Assurez-vous d'avoir installé les prérequis suivants avant d'exécuter le projet :

- Python 3.7 ou plus récent
- [TensorFlow](https://www.tensorflow.org/install)
- [Streamlit](https://docs.streamlit.io/en/stable/installation.html)
- [Trimesh](https://trimsh.org/)
- [PyVista](https://docs.pyvista.org/)

Vous pouvez installer les dépendances nécessaires en utilisant `pip` :

bash
```pip install tensorflow streamlit trimesh pyvista scipy```


## Installation
1-Clonez ce dépôt sur votre machine locale :
git clone https://github.com/votre-utilisateur/3D-Teeth-Classification.git
cd 3D-Teeth-Classification
2-Assurez-vous d\'avoir installé les dépendances mentionnées dans la section "Prérequis".

3-Placez le modèle pré-entraîné teeth_classification_model.h5 dans le répertoire racine du projet.
***

Pour exécuter l'application Streamlit, utilisez la commande suivante :

```streamlit run app.py```
Cela lancera l'application web dans votre navigateur par défaut.

## Fonctionnement

1-Téléchargement du fichier 3D : Téléchargez un fichier .obj de dent en utilisant l'interface de téléchargement.
2-Classification : Une fois le fichier téléchargé, l'application classifie la dent et affiche les probabilités pour chaque catégorie.
3-Visualisation 3D : Visualisez le modèle 3D de la dent et explorez la vue à 360 degrés.
Structure du Projet :
C:\Users\abdel\Desktop\111\
│
├── data_preparation.ipynb
├── model_training.ipynb
├── app.py
├── model_testing.ipynb
│
└── data\
    ├── Canine\
    ├── Deuxieme_molaire\
    ├── Deuxieme_premolaire\
    ├── Incisive_centrale\
    ├── Incisive_laterale\
    ├── Premiere_molaire\
    └── Premiere_premolaire\

   ## Remarques
Modèle : Le modèle de classification a été entraîné sur un jeu de données 3D spécifique. Pour obtenir des résultats optimaux, assurez-vous que les fichiers .obj téléchargés respectent les mêmes standards de prétraitement.
Limitations : Le fichier téléchargé doit être un fichier .obj valide et de taille inférieure à 200MB pour garantir un traitement efficace.

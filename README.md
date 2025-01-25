# Classification des Dents en 3D avec ConvNet
## Introduction
Ce projet, réalisé en collaboration avec 3D Smart Factory, utilise des réseaux de neurones convolutifs (ConvNet) pour classifier des modèles de dents en 3D. Il combine l'expertise industrielle en imagerie 3D avec des techniques avancées d'apprentissage profond pour améliorer la précision et l'efficacité des diagnostics dentaires.

## Fonctionnalités
- **Classification de dents 3D** : Chargez un fichier `.obj` de dent 3D, et l'application le classifie parmi les catégories suivantes : Canine, Deuxième molaire, Deuxième prémolaire, Incisive centrale, Incisive latérale, Première molaire, Première prémolaire.
- **Visualisation 3D** : Permet d'explorer le modèle 3D en temps réel, avec des vues à 360 degrés.
- **Prédictions en temps réel** : L'application offre une classification instantanée dès que le modèle 3D est téléchargé.
- **Prise en charge de plusieurs formats de fichiers** : En plus des fichiers `.obj`, l'application prend également en charge les fichiers `.stl` et `.ply`.
- **Téléchargement des résultats** : Les utilisateurs peuvent télécharger les résultats de classification au format JSON, y compris les probabilités associées à chaque catégorie.
- **Comparaison de modèles** : Possibilité de comparer visuellement plusieurs modèles de dents simultanément pour détecter les différences.
- **Historique des téléchargements** : Gardez une trace des modèles de dents précédemment téléchargés et classifiés pour les consulter ultérieurement.
- **Amélioration des performances** : Optimisation de la gestion des fichiers volumineux pour garantir une manipulation fluide même pour des fichiers 3D complexes.

## Prérequis
Assurez-vous d'avoir installé les prérequis suivants avant d'exécuter le projet :
- Python 3.7 ou plus récent
- [TensorFlow](https://www.tensorflow.org/install)
- [Streamlit](https://docs.streamlit.io/en/stable/installation.html)
- [Trimesh](https://trimsh.org/)
- [PyVista](https://docs.pyvista.org/)

Vous pouvez installer les dépendances nécessaires en utilisant `pip` :

```bash
pip install tensorflow streamlit trimesh pyvista scipy
```

## Installation
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/3D-Teeth-Classification.git
   cd 3D-Teeth-Classification
   ```
2. Assurez-vous d'avoir installé les dépendances mentionnées dans la section "Prérequis".
3. Placez le modèle pré-entraîné `teeth_classification_model.h5` dans le répertoire racine du projet.

## Utilisation
Pour exécuter l'application Streamlit, utilisez la commande suivante :
```bash
streamlit run app.py
```
Cela lancera l'application web dans votre navigateur par défaut.

### Fonctionnement
1. **Téléchargement du fichier 3D** : Téléchargez un fichier .obj, .stl ou .ply de dent en utilisant l'interface de téléchargement.
2. **Classification** : L'application classifie la dent et affiche les probabilités pour chaque catégorie.
3. **Visualisation 3D** : Visualisez le modèle 3D de la dent et explorez la vue à 360 degrés.
4. **Téléchargement des résultats** : Téléchargez les résultats sous format JSON après la classification.
5. **Comparaison de modèles** : Ajoutez plusieurs fichiers 3D pour une comparaison simultanée.

## Structure du Projet
```
C:\Users\abdel\Desktop\3D_Teeth_Classification\
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
```

## Remarques
- **Modèle** : Le modèle de classification a été entraîné sur un jeu de données 3D spécifique. Pour obtenir des résultats optimaux, assurez-vous que les fichiers téléchargés respectent les mêmes standards de prétraitement.
- **Limitations** : Le fichier téléchargé doit être un fichier .obj, .stl, ou .ply valide et de taille inférieure à 200MB pour garantir un traitement efficace.
- **Performances** : L'application est optimisée pour gérer les modèles 3D volumineux sans compromettre les performances. Toutefois, la vitesse de traitement dépend de la taille du modèle et des ressources système.

## Contribution
Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
## Contact
Pour toute question ou suggestion, veuillez contacter :
- [Ennajari Abdellah] - [abdellahennajari2018@gmail.com]
- [3D Smart Factory] - [contact@3dsmartfactory.com]

---

Développé en collaboration avec 3D Smart Factory.

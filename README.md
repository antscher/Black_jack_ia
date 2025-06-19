# Black Jack IA

Bienvenue dans **Black Jack IA**, un projet innovant qui explore l'intelligence artificielle appliquée au jeu de Black Jack à travers l'apprentissage par renforcement.

## Présentation du projet

Ce projet a été continué sur un autre repository (cf fin de page)

Ce projet vise à développer une intelligence artificielle capable de jouer au Black Jack de manière optimale. Nous avons mis en œuvre des techniques avancées d'apprentissage par renforcement pour permettre à l'IA d'apprendre, s'adapter et s'améliorer au fil des parties.

## Points forts

- **Apprentissage par renforcement** : L'IA apprend à partir de ses propres expériences, en recevant des récompenses ou des pénalités selon ses actions.
- **Environnement simulé** : Un environnement de jeu fidèle a été créé pour permettre à l'IA de s'entraîner efficacement.
- **Optimisation des stratégies** : L'IA découvre et affine des stratégies gagnantes sans intervention humaine directe.
- **Visualisation des progrès** : Des outils de suivi permettent d'observer l'évolution des performances de l'IA au fil du temps.

## Technologies utilisées

- Python 
- Pas de bibliotheque d'apprentissage
- Outils de visualisation (pas devellopés)

## Comment démarrer

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/Black_jack_ia.git
   ```
2. Installez les dépendances 

3. Lancez l'entraînement de l'IA 

## Limites rencontrées

Malgré la mise en place de l'apprentissage par renforcement, les résultats obtenus n'ont pas été pleinement convaincants. Deux principales raisons expliquent ces limites :

- **Durée d'entraînement** : L'apprentissage par renforcement nécessite un très grand nombre de parties pour converger vers une stratégie optimale. Les temps d'entraînement se sont révélés particulièrement longs avec Python.
- **Gestion du multithreading** : Python présente des limitations importantes pour le calcul parallèle intensif, notamment à cause du GIL (Global Interpreter Lock), ce qui a freiné l'accélération de l'entraînement via le multithreading.

## Vers une version Rust

Pour surmonter ces obstacles, nous avons créé un nouveau dépôt reprenant ce projet, mais entièrement réécrit en **Rust**. Ce langage permet une gestion efficace du multithreading et des performances nettement supérieures pour ce type de simulation intensive.

👉 [Voir le dépôt Rust](lien_vers_le_repo_rust)


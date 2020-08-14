# OpenClassrooms Projet 8: Créez une plateforme pour amateurs de Nutella

Ce répertoire contiendra les développents du projet 8. L'objectif du projet est de développer pour la société Pub Beurre une plateforme web à destination de ses clients selon un cahier des charges.

## Fonctionnalités Attendues

- Développement avec le Framework Web Django
- Récupération des données sur l’API Open Food Facts
- Affichage du champ de recherche dès la page d’accueil 
- Authentification de l’utilisateur par son adresse mail
- Base de données PostgreSQL
- Déploiement sur Heroku
- Ecriture de tests

## Structure du projet Django

Le projet Django pubbeurre contient 5 applications, permettant de remplir les fonctionnalités attendues par le client:

- **openfoodfacts:** Récupération et intégrations en base des données de l’API Open Food Facts. Ne contient qu'une custom command lancant les traitements.
- **app:** Application centralisant les éléments globaux du projet (CSS, fichiers statiques, templates généraux et javascript)
- **product:** Gestion de la recherche et de l’affichage des produits.
- **substitute:** Gestion et affichage des produits de substitution favoris d’un utilisateur.
- **user:** Gestion et affichage de la création et de la connexion des utilisateurs.

## Déploiement et utilisation du site en local

Nécessite Python 3.7 et pipenv d'installés sur le poste, effectuer les manipulations suivantes dans l'ordre:

  1. Récupérer le projet Django depuis github.
  2. Installer l'environnement virtuel `pipenv install`
  3. Entrer dans l'environnement virtuel `pipenv shell`
  4. Récupérer la structure de la base de données avec `python manage.py migrate`
  5. Lancer la custom command fill_database, permettant de récupérer les données de l'API OpenFoodFacts `python manage.py fill_database`
  6. Lancer le serveur `python manage.py runserver`
  
Le projet est configuré de sorte à utiliser une base de données SQLite en local, PostgreSQL n'est mis en place et utilisé que sur le site en production sur Heroku à l'adresse https://ango-oc-purbeurre.herokuapp.com/

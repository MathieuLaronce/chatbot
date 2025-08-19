# CGVBot

![Python](https://img.shields.io/badge/python-3.9+-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green)

## Table des matières
1. [À propos](#à-propos)  
2. [Fonctionnalités](#fonctionnalités)  
3. [Prérequis](#prérequis)  
4. [Technologies](#technologies)  
5. [Utilisation](#utilisation)  
6. [Développement](#développement)  
7. [Licence](#licence)
8. [Créateurs](#Créateurs) 

---

## À propos
**CGVBot** est un chatbot interne conçu pour **MonEshop** afin d’automatiser les réponses aux questions sur les Conditions Générales de Vente : paiement, rétractation, livraison, garantie et données personnelles.  

Il utilise une base SQLite pour stocker l’historique des interactions et un modèle IA fine-tuné pour générer des réponses précises et contextualisées.  

---

## Fonctionnalités
- Réponses automatiques aux questions sur les CGV.  
- Pré-prompt métier intégré pour contextualiser les réponses.  
- Base de données SQLite avec journalisation des prompts et réponses.  
- Chatbot rapide à exécuter depuis la console.  

---

## Prérequis
- Python >= 3.9  
- SQLite  
- Docker (optionnel, pour Adminer et gestion de la base de données)  
- Bibliothèques Python listées dans `requirements.txt`  

---

## Technologies
- **Langage** : Python  
- **Base de données** : SQLite  
- **Conteneurisation** : Docker (Adminer pour visualiser la BDD)  
- **Modèle IA** : fine-tuning OpenAI via fichier JSONL  

---

## Utilisation
- Lancer `app3.py` pour démarrer le chatbot.  
- Saisir vos questions sur les CGV dans la console.  
- Les réponses sont affichées et enregistrées automatiquement dans la table `logs`.  
- Pour adapter le chatbot, modifier le fichier JSONL ou le pré-prompt dans le code.  

---

## Développement
- Versions disponibles : `app.py`, `app2.py`, `app3.py` (version stable recommandée).  
- Ajouter de nouvelles clauses dans la base ou le fichier JSONL pour enrichir les réponses.  
- Respecter les bonnes pratiques : modularité, commentaires, lisibilité.  

---

## Licence
Ce projet est sous **licence MIT**. 

## Créateurs

- [Mathieu Laronce](https://github.com/MathieuLaronce)
- [Hugo Babin](https://github.com/hugobabin)


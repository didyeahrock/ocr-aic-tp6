# ocr-aic-tp6
**Auteur 	:** 	Didier Lemaitre

**Version	:**	1.0

**Date	:**	2021-06-06

Travail effectué dans le cadre de la formation Administrateur Infrastructure et Cloud 
d'OpenClassrooms, projet numéro 6.

L'objectif demandé est de produire du code python permettant l'automatisation de tâche d'administration système.

Ici l'ensemble des scripts permet d'installer un serveur Wordpress sur une base LAMP dans un environnement Debian 10 et de configurer le https à l'aide d'un certificat auto-signé.

Le choix de garder un certificat auto-signé et de ne pas utiliser d'outils comme letsencrypt ou certbot se justifie par l'absence de nom de domaine publique. Dans un environnement professionel il sera possible de se simplifier la tâche en s'appuyant notamment sur certbot.

### installation-prerequis.py
Le premier script "installation-prerequis.py" comme son nom l'indique sert à installer les différents paquets nécessaires au bon fonctionnement du script ainsi que la base LAMP.
Ce script se termine par l'exécution de la commande "mysql_secure_connexion" qui va demander d'effectuer des choix sur la configuration MariaDB, notamment de modifier ou non le mot de passe root de la base.

### configuration-https.py
Le deuxième script "configuration-https.py" sert à préparer https dans apache.
Il génère un groupe Diffie Hellmann si celui-ci n'existe pas et crée également un fichier de configuration apache pour SSL.

### configuration-wordpress.py
Le troisième script "configuration-wordpress.py" sert à configurer la base MariaDB et produire les fichiers de conf apache et wordpress. Les différents identifiants et mots de passe sont saisis par l'utilisateur durant l'exécution du script.

### full-install.py
Ce dernier script rassemble l'exécution des trois scripts précédents pour n'avoir qu'une seule commande à lancer

### Logs
Chaque script crée son propre fichier de log éponyme à la racine du projet.
Les erreurs rencontrés lors de l'exécution du script sont normalement remontées dans ces même fichiers.


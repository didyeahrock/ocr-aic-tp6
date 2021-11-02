#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
    installation-prerequis.py
    Script effectuant les installations de paquets nécessaire à l'installation d'un serveur LAMP
    + Wordpress

    Auteur :    Pierre LEMAIRE
    Version :   0.1
    Date :      2021-05-11

    Testé avec Python 3.7 sous Debian 10 (Buster) stable

"""

#Importation des modules nécessaires

import logging
import subprocess
import os

"""
    Paquets à installer : 
        apache2
        php
        mariadb-server
        curl
        wordpress
        python3
        module python validators
        module python mariadb
        pip

    Configuration de base :
        mysql_secure_installation

"""

#Définitions des constantes

LOG_FILE = "./installation.log"

#Configuration du fichier de log

try:
    logging.basicConfig(filename=LOG_FILE, format="%(asctime)s : %(levelname)s:%(message)s", 
        level=logging.DEBUG)
    logging.info("Début de l'installation des pré-requis")
except Exception as e:
    print("Erreur lors de la création du fichier de journalisation")
    raise e

#Mise à jour du système et Installation des paquets

try:
    logging.info("Mise à jour du sytème et installation des paquets...")
    os.system("apt update ; apt upgrade")
    os.system("apt install apache2 php mariadb-server wordpress curl python3 python3-pip libmariadbclient-dev pip")
    os.system("pip3 install --upgrade setuptools")
    os.system("pip3 install validators")
    os.system("pip3 install mariadb")
    os.system("mysql_secure_installation")
    logging.info("Mises à jour et installations réalisées avec succès")
    exit(0)
except Exception as e:
    print("Echec de l'installation des paquets")
    logging.error("Echec de l'installation des paquets")
    logging.error(e)
    raise e

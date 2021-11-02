#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
  full-install.py
  Script principal rassemblant l'exécution des scripts suivants : 
    - installation-prerequis.py
    - configuration-https.py
    - configuration-wordpress.py
"""

#Importation des modules nécessaires

import subprocess

try:
  #Lancement du 1er script : installation-prerequis.py
  subprocess.run(["python3","installation-prerequis.py"])
  #Lancement du 2e script : configuration-https.py
  subprocess.run(["python3","configuration-https.py"])
  #Lancement du 3e script : configuration-wordpress.py
  subprocess.run(["python3","configuration-wordpress.py"])
  
except Exception as e:
  raise e

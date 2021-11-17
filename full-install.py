#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
  full-install.py
  Main Script  
    - installation-prerequis.py
    - configuration-https.py
    - configuration-glpi.py
"""

# Import of the required modules

import subprocess

try:
  #Lancement du 1er script : installation-prerequis.py
  subprocess.run(["python3","installation-prerequis.py"])
  #Lancement du 2e script : configuration-https.py
  subprocess.run(["python3","configuration-https.py"])
  #Lancement du 3e script : configuration-wordpress.py
  subprocess.run(["python3","configuration-glpi.py"])
  
except Exception as e:
  raise e

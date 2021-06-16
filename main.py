#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice

# Lee el fichero con las frases
archivo_con_frases = open("frases.txt", "r")
# Lee las líneas
lineas = archivo_con_frases.readlines()
# Limpia los saltos de línea
frases = tuple(map(lambda linea: linea.strip(), lineas))


print(choice(frases))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice
import os

# Variables
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHANNEL_ID = os.environ['TELEGRAM_CHANNEL_ID']
TELEGRAM_URL_SEND = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Lee el fichero con las frases
archivo_con_frases = open("frases.txt", "r")
# Lee las líneas
lineas = archivo_con_frases.readlines()
# Limpia los saltos de línea
frases = tuple(map(lambda linea: linea.strip(), lineas))
# Obtiene frase aleatoria
frase_aleatoria = choice(frases)
# Envía al canal
os.system(f"curl -s -X POST https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id={TELEGRAM_CHANNEL_ID} -d text='{frase_aleatoria}'")

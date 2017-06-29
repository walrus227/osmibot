import requests
import sys
import os
import platform
import pip
import time

useros = platform.system()
var = 1

def install(package):
    pip.main(['install', package])
while var == 1:
    os.system('cls')
    print('Osmibot Launcher v1.0')
    print('Select an option:')
    print('_____________________')
    print('1. Run Osmibot')
    print('2. Run Osmibot with autorestart in case of errors.')
    print('3. Install dependencies')
    print('4. Exit')
    choice = input('Enter option number and press enter:')
    if choice == '1':
        import osmibot

    if choice == '2':
        if useros == 'Windows':
            os.system('autorestart.bat')
        else:
            print('Currently only supported on Windows.')

    if choice == '3':
        install('discord.py')

    if choice == '4':
        sys.exit()

    if choice == '69':
        print('Commencing Countdown, engines on...')
        time.sleep(2)

import requests
import sys
import os

def install(package):
        pip.main(['install', package])

print 'Osmibot Launcher v1.0'
print 'Select an option:'
print '_____________________'
print '1. Run Osmibot'
print '2. Run Osmibot with autorestart in case of errors.'
print '3. Install dependencies'
choice = input('Enter option number and press enter:')
if choice == '1':
    import osmibot

if choice == '2':
    os.system('autorestart.bat')

if choice == '3':
    install('discord.py')
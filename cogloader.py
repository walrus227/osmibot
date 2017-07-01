import platform
import os
import zipfile
import shutil
import sys
import time
try:
    import wget
except ImportError:
    print('Please install Osmibot before running the Cog Loader.')
    input('Press enter to exit.')
    sys.exit()

def clear():
    """Clears Shell."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def title(window: str = None):
    """Renames current shell Window.

    Currently only supported on Windows."""
    if str is None:
        print('Please input a window title.')
    else:
        if platform.system() == 'Windows':
            os.system('title ' + window)
        else:
            pass

while True:
    clear()
    title('Osmibot Cog Loader')
    print('Osmibot Cog Loader v1.0')
    print('________________________________')
    print('1. Download/Update Repo')
    print('2. Install Cog from Repo')
    print('3. Exit')
    choice = input('Enter choice number: ')
    if choice == '1':
        clear()
        repo = input('Enter repo name here: ')
        wget.download('https://github.com/ANT1H3R0/cogrepo/raw/master/' + repo + '.zip')
        if os.path.exists(repo):
            shutil.rmtree(repo)
        os.mkdir(repo)
        zip_ref = zipfile.ZipFile(repo + '.zip', 'r')
        zip_ref.extractall(repo)
        zip_ref.close()
        os.remove(repo + '.zip')
    if choice == '2':
        clear()
        repo = input('Enter repo name here: ')
        cog = input('Enter cog name here: ')
        if not os.path.exists(repo):
            print('Repo not downloaded.')
            time.sleep(2)
        elif not os.path.exists(repo + '/' + cog + '.py'):
            print("Cog doesn't exist.")
            time.sleep(2)
        else:
            print('Installing cog...')
            if not os.path.exists('cogs'):
                print("Cogs folder doesn't exist. Creating it...")
                os.mkdir('cogs')
            try:
                shutil.copy(repo + '/' + cog + '.py', 'cogs/' + cog + '.py')
                print('Successfully installed Cog')
                time.sleep(2)
            except Exception as e:
                print('Error!')
                print(e)
                input('Press enter to continue...')
    if choice == '3':
        sys.exit()

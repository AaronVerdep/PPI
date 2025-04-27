import os
import time
import requests
import shutil

# Expansión de la ruta para bashrc y ppi.py
bashrc_path = os.path.expanduser('~/.bashrc')
ppi_path = os.path.expanduser('~/ppi.py')
homeusr_path = os.path.expanduser('~')

def install():
    os.system('clear')
    print('-')
    time.sleep(0.1)
    os.system('clear')
    print('/')
    time.sleep(0.1)
    os.system('clear')
    print('|')
    time.sleep(0.1)
    os.system('clear')
    print('\\')
    time.sleep(0.1)
    os.system('clear')
    print('-')

    shutil.copy(bashrc_path, f'{homeusr_path}/.bashrcsecurecopy')

    with open(bashrc_path, 'a') as bashrc:
        bashrc.write('\nalias ppi="python3 ~/ppi.py"\n')

    with open(ppi_path, 'w') as ppi:
        ppi.write('''
import os
import time
import requests

os.system('clear')
print('PPI:')
print('1. Install Module')
print('2. List Modules')
print('3. Update Installer')
print('4. Exit')
print()
choice = input('> ')
if choice == '1':
    os.system('clear')
    print('Enter the module name:')
    moduleinput = input('> ')
    os.system('clear')
    print('Installing Module: ' + moduleinput)
    module = requests.get(f'https://raw.githubusercontent.com/zerousers-dev/PPI/refs/heads/main/pkgs/{moduleinput}.py')
    if module.status_code == 200:
        with open(f'/home/{os.getlogin()}/{moduleinput}.py', 'wb') as f:
            f.write(module.content)
        print('We need Sudo permissions to install the module to python libs.')
        os.system(f'sudo mv /home/{os.getlogin()}/{moduleinput}.py /usr/lib/python3.12/{moduleinput}.py')
        os.system('clear')
        print('Module Installed!')
    else:
        print('Module not found. Please check the module name and try again.')
        input()
        os.system('clear')
        print('Exiting...')
        exit()
elif choice == '2':
    os.system('clear')
    url = "https://api.github.com/repos/zerousers-dev/PPI/contents/pkgs"
    response = requests.get(url)
    
    if response.status_code == 200:
        files = response.json()
        for file in files:
            print(file['name'])
    else:
        print("Error:", response.status_code)
    input('')
elif choice == '3':
    os.system('clear')
    print('Getting installer.py')
    installer = requests.get('https://raw.githubusercontent.com/zerousers-dev/PPI/refs/heads/main/installer.py')
    with open('installer.py', 'wb') as updinstaller:
        updinstaller.write(installer.content)
    os.system('clear')
    print('Updated!')
    exit()
elif choice == '4':
    os.system('clear')
    exit()
''')

    print('Installed PPI!')
    print('PPI is now installed! You can use it by typing "ppi" in the terminal.')
    input()
    exit()

os.system('clear')
print('[------------PPI INSTALLER-------------]')
print('Welcome to PPI Installer!')
print('This is a Linux Mint Program where you can download Python Modules for Python 3.12!')
print('(From GitHub made by AaronVerdep)')
print()
print('Press enter to continue.')
input()
os.system('clear')
print('[---REQUIREMENTS---]')
print('This program requires the following Python modules:')
print('1. os')
print('2. time')
print('3. requests')
print()
print('Press enter to continue.')
input()
os.system('clear')
print('[---PPI---]')
print('1. Install PPI')
print('2. Exit')
print()
choice = input('> ')
if choice == '1':
    os.system('clear')
    install()
elif choice == '2':
    os.system('clear')
    print('Exiting...')
    exit()
else:
    os.system('clear')
    print('Invalid choice. Exiting...')
    exit()

# menu.py
import os

menu_data = {
    'options': []  # each option has 'label' and 'function'
}

def add_option(label, function):
    menu_data['options'].append({'label': label, 'function': function})

def display_menu():
    os.system('clear')
    print("MENU:")
    for i, option in enumerate(menu_data['options']):
        print(f"{i + 1}. {option['label']}")
    choice = input("> ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(menu_data['options']):
            menu_data['options'][index]['function']()
            return
    os.system('clear')
    print("Invalid option.")
    input('')

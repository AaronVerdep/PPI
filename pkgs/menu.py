# menu.py
import os

menu_data = {
    'options': []  # each option has 'label' and 'function'
}
title = "MENU"

def add_option(label, function):
    menu_data['options'].append({'label': label, 'function': function})

def display_menu():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"{title}:")
    for i, option in enumerate(menu_data['options']):
        print(f"{i + 1}. {option['label']}")
    print()
    choice = input("> ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(menu_data['options']):
            menu_data['options'][index]['function']()
            return
    os.system('clear' if os.name != 'nt' else 'cls')
    print("Invalid option.")
    input('')

def set_title(settitle):
    global title
    title = settitle

def clear_menu():
    global menu_data
    menu_data = {
        'options': []
    }

def reset_menu():
    global title, menu_data
    title = "MENU"
    menu_data = {
        'options': []
    }

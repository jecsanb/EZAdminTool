from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import *

def build_submenu(title, parent):
    return build_menu(title, parent)


def build_selection_submenu(title, parent, options):
    menu = SelectionMenu(options, title)
    menu = SubmenuItem(title, submenu=menu, menu=parent)
    return menu


def build_menu(title, parent=None):
    menu = ConsoleMenu(title)
    if parent is not None:
        menu = SubmenuItem(title, submenu=menu, menu=parent)
    return menu


def write_to_screen(screen, prompt):
    screen.println(prompt)


def get_input_from_screen(screen, prompt):
    screen.input(prompt=prompt)


def add_menu_options(menu, options):
    for option in options:
        menu.append_item(option)
    return menu

from consolemenu import ConsoleMenu
from consolemenu.items import *


def build_submenu(title, parent):
    return build_menu(title, parent)


def build_menu(title, parent=None):
    menu = ConsoleMenu(title)
    if parent is not None:
        menu = SubmenuItem(title, submenu=menu, menu=parent)

    return menu


def add_menu_options(menu, options):
    for option in options:
        menu.append_item(option)
    return menu

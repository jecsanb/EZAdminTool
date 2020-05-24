from consolemenu import *

from config import configurations_submenu
from menu_helper import build_menu, add_menu_options


def account_management_submenu(parent):
    menu = build_menu("Account Management", parent)
    return menu


def main():
    main_menu = ConsoleMenu("Main Menu")
    options = [configurations_submenu(main_menu)]
    add_menu_options(main_menu, options)
    main_menu.show()


if __name__ == '__main__':
    main()

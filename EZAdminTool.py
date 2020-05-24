from consolemenu import *

from account_managment import account_management_submenu
from config_menus import configurations_submenu
from menu_helper import add_menu_options

CONSOLE_SCREEN = Screen()


def main():
    main_menu = ConsoleMenu("EZAdmin Tool", subtitle="Main Menu", prologue_text="Select an action.",
                            epilogue_text="Copyright Jecsan Blanco under MIT License", screen=CONSOLE_SCREEN)
    options = [account_management_submenu(parent=main_menu), configurations_submenu(parent=main_menu)]
    add_menu_options(main_menu, options)
    main_menu.show()


if __name__ == '__main__':
    main()

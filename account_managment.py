from consolemenu.console_menu import ConsoleMenu
from consolemenu.items import FunctionItem
from consolemenu.prompt_utils import PromptUtils

from menu_helper import add_menu_options, build_menu


def ask_for_account_username(screen):
    return prompt_for_input(screen, "Enter Account Username")


def print_to_screen(screen, prompt):
    pu = PromptUtils(screen)
    pu.println(prompt)
    pu.enter_to_continue()


def create_account(screen):
    account = ask_for_account_username(screen)
    print_to_screen(screen, f"Account {account} Deleted, (jk not this is not implemented")


def modify_account(screen):
    account = ask_for_account_username(screen)
    print_to_screen(screen, f"Account {account} Deleted, (jk not this is not implemented")


def delete_account(screen):
    account = ask_for_account_username(screen)
    print_to_screen(screen, f"Account {account} Deleted, (jk not this is not implemented")


def prompt_for_input(screen, prompt):
    pu = PromptUtils(screen)
    return pu.input(prompt=prompt, quit_message="Enter q to cancel").input_string


def account_management_submenu(parent):
    title = "Account Management"
    menu_options = [FunctionItem("Create Account", create_account, args=[parent.screen]),
                    FunctionItem("Modify Account", modify_account, args=[parent.screen]),
                    FunctionItem("Delete Account", delete_account, args=[parent.screen])]
    menu = build_menu(title, parent)
    add_menu_options(menu.submenu, menu_options)
    return menu


def main():
    menu = ConsoleMenu()
    sub_menu = account_management_submenu(menu)
    add_menu_options(menu, [sub_menu])
    menu.show()


if __name__ == '__main__':
    main()

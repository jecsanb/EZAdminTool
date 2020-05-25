from consolemenu.console_menu import ConsoleMenu
from consolemenu.items import FunctionItem
from consolemenu.prompt_utils import PromptUtils


class AccountManagement:

    def __init__(self):
        self.menu = self.__build_menu()
        self.prompt_utils = PromptUtils(self.menu.screen)

    def __build_menu(self):
        menu_title = "Account Management"
        menu_options = [FunctionItem("Create Account", self.create_account_option),
                        FunctionItem("Modify Account", self.modify_account_option),
                        FunctionItem("Delete Account", self.delete_account_option)]
        menu = ConsoleMenu(menu_title)
        for option in menu_options:
            menu.append_item(option)
        return menu

    def print_placeholder(self):
        self.print_to_console("Did the thing!")

    def create_account_option(self):
        username = self.prompt_for_account_username()
        self.print_placeholder()

    def modify_account_option(self):
        username = self.prompt_for_account_username()
        self.print_placeholder()

    def delete_account_option(self):
        username = self.prompt_for_account_username()
        self.print_placeholder()

    def prompt_on_console(self, prompt):
        self.prompt_utils.input(prompt)

    def print_to_console(self, message):
        self.prompt_utils.println(message)
        self.prompt_utils.enter_to_continue()

    def prompt_for_account_username(self):
        return self.prompt_on_console("Enter Account Username")


def main():
    am = AccountManagement()
    am.menu.show()


if __name__ == '__main__':
    main()

import configparser
import os
import platform
import subprocess

from consolemenu import PromptUtils, ConsoleMenu
from consolemenu.items import FunctionItem

APP_NAME = 'EZAdminTool'
CONFIG_FILE_NAME = f'{APP_NAME}.config.txt'
DEFAULT_CONFIG_PATH = './' + CONFIG_FILE_NAME
DEFAULT_TEXT_EDITORS = {'Linux': 'gedit', 'Windows': 'notepad.exe'}

DEFAULT_CONFIG_STRING = \
"""
# Configuration file for EZAdmin tool.
[ezadmin]
# Set to True once updated with correct settings.
configured : False
config_path : ./EZAdminTool.config.txt

[Server]
# Server accepts IP Address or FQDN assuming DNS can resolve and default to default LDAP port.
host_name : sample_server
port : 389

[LDAP_SEARCH_PATHS]
# The organization units where to search for users and groups.
0 : OU=Users,DC=sample,DC=com
1 : OU=Other,DC=sample,DC=com
2 : OU=Other2,DC=sample,DC=com

[Authentication]
# Used to authenticate to the directory server
authentication_domain : sample.com
username : sample
password : password"""


class ConfigurationManagement:
    def __init__(self):
        self.menu = self.__build_menu()
        self.console = PromptUtils(self.menu.screen)

        self.active_configs = configparser.ConfigParser(delimiters=':')
        self.active_configs.read(DEFAULT_CONFIG_PATH)

        if len(self.active_configs.sections()) == 0:
            self.__save_default_configs()
            self.refresh_active_configurations()

        self.default_editor = DEFAULT_TEXT_EDITORS[platform.system()]

        if not self.configured():
            self.ask_to_configure()

    def __build_menu(self):
        menu_title = "Configuration"
        menu_options = [FunctionItem("View / Edit Configuration", self.view_or_edit_configuration),
                        FunctionItem("Test Configurations", self.test_configuration)]
        menu = ConsoleMenu(menu_title)
        for option in menu_options:
            menu.append_item(option)
        return menu

    def configured(self):
        return self.active_configs['ezadmin'].getboolean('configured')

    def ask_to_configure(self):
        configure = self.console.prompt_for_yes_or_no(
            "Settings dont appear to be configured, do you want to configure them now?")
        if configure:
            self.view_or_edit_configuration()
        else:
            self.console.println("Application will not work properly without configuration.")
            self.console.enter_to_continue()

    def __save_default_configs(self):
        with open(DEFAULT_CONFIG_PATH, 'w') as configfile:
            configfile.write(DEFAULT_CONFIG_STRING)

    def view_or_edit_configuration(self):
        if not os.path.exists(DEFAULT_CONFIG_PATH):
            # configuration file does not exist, default configs created
            self.__save_default_configs()
        self.open_config_file_with_editor_and_wait()
        self.refresh_active_configurations()

    def refresh_active_configurations(self):
        self.active_configs = configparser.ConfigParser(delimiters=':')
        self.active_configs.read(DEFAULT_CONFIG_PATH)

    def open_config_file_with_editor_and_wait(self):
        # Check on security concerns for doing this.
        pr = subprocess.Popen(f'{self.default_editor} {os.path.normpath(DEFAULT_CONFIG_PATH)}')
        self.console.println("Close configurations to continue...")
        pr.communicate()

    def test_configuration(self):
        self.console.println("Testing configuration ...")
        self.console.enter_to_continue()


def main():
    config_man = ConfigurationManagement()
    config_man.menu.show()


if __name__ == '__main__':
    main()

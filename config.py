import configparser
import os
import platform
import subprocess

from consolemenu.items import FunctionItem

from menu_helper import build_submenu, add_menu_options

DEFAULT_CONFIG_PATH = './'
CONFIG_FILE_NAME = 'ezadmin.config.txt'
CONFIG_PATH = DEFAULT_CONFIG_PATH + CONFIG_FILE_NAME

DEFAULT_TEXT_EDITORS = {'Linux': 'gedit', 'Windows': 'notepad.exe'}

DEFAULT_CONFIG = \
    '''
    [ezadmin]
    # Set to True once updated with correct settings.
    configured : False
    
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
    password : password
    '''


def create_default_config():
    config = configparser.ConfigParser(delimiters=':')
    config.read_string(DEFAULT_CONFIG)
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)
    print("Configuration file created, please configure: ", CONFIG_PATH)


def view_or_edit_configuration():
    if not os.path.exists(CONFIG_PATH):
        create_default_config()
    open_file_with_editor_and_wait(os.path.normpath(CONFIG_PATH), DEFAULT_TEXT_EDITORS[platform.system()])


def configurations_submenu(parent):
    menu = build_submenu("Configurations", parent)
    menu_options = [FunctionItem("View / Edit Configuration", view_or_edit_configuration, menu=menu)]
    add_menu_options(menu.submenu, menu_options)
    return menu


def open_file_with_editor_and_wait(file_path,editor):
    print("Opening ", file_path)
    # Check on security concerns for doing this.
    pr = subprocess.Popen(f'{editor} {file_path}')
    print("Close file to continue...")
    pr.communicate()


def main():
    view_or_edit_configuration()


if __name__ == '__main__':
    main()

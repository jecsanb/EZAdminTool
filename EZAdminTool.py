import configparser
DEFAULT_CONFIG_PATH = './'
CONFIG_FILE_NAME = 'ezadmin.config'

def show_menu(menu_title="Menu", menu_options=None):
    """
    Displays a text based menu and executes the code associated with the option.
    :param menu_title: The title to display
    :param menu_options:  The option to display and function to execute.
    """
    if menu_options is None:
        menu_options = dict()
    menu_bar = 10 * "="
    while True:
        print(f'{menu_bar} {menu_title} {menu_bar}')
        for i, menu_option in enumerate(menu_options.keys()):
            print(f'[{i}] Enter {i} for {menu_option}')
        print(f'Enter \'q\' to return.')
        selection = input("Make a selection: ")
        if selection.lower() == 'q':
            break
        elif int(selection) in range(0, len(menu_options)):
            list(menu_options.values())[int(selection)]()
    clear()


def account_management_menu():
    title = "User Management"
    menu_options = {"Create User(s)": place_holder, 'Disable User(s)': place_holder, 'Delete User(s)': place_holder,
                    'Display User Details': place_holder, 'Edit User Details': place_holder}
    show_menu(title, menu_options)


def place_holder():
    print("Place holder selected")
    pass


def group_management_menu():
    title = "Groups and OU Management"
    menu_options = {"Create New Group(s)": place_holder, "Delete Group(s)": place_holder,
                    "List Group(s) Members": place_holder, "Add Members To Group(s)": place_holder}
    show_menu(title, menu_options)


def ad_management_menu():
    title = "AD Management"
    menu_options = {'Manage Users': account_management_menu, "Manage Groups": group_management_menu}
    show_menu(title, menu_options)


def reports_menu():
    title = "Reports"
    menu_options = {'Active Accounts': place_holder, 'Inactive Accounts': place_holder,
                    'Administrator Accounts': place_holder, 'Members of': place_holder, 'Custom Reports': place_holder}
    show_menu(title, menu_options)


def main_configuration_menu():
    title = "Configuration"
    menu_options = {'View Configurations': place_holder, 'Open Configurations': place_holder}
    show_menu(title, menu_options)


def main_menu():
    title = "EZAdmin Tool"
    menu_options = {'AD Management': ad_management_menu, 'Reports': reports_menu,
                    'Configuration': main_configuration_menu}
    show_menu(title, menu_options)


def try_auto_config(config):
    pass


def get_default_configs():
    config = configparser.ConfigParser()
    config['CONNECTION'] = {'AuthenticationDomain': 'domain.local',
                            'LDAPSearchPath': 'OU=Users,DC=domain,DC=local',
                            'HostName': 'localhost', 'Port': '636',
                            'Username': 'Administrator'}
    try_auto_config(config)
    return config


def save_config(config, file_name, path=None):
    with open(file_name, 'w') as configfile:
        config.write(configfile)


def edit_configurations(config):
    # display configurations
    # prompt which to edit
    # apply edit
    # ask y to save
    pass


def load_configs():
    try:
        pass
        # try to load configuration file as set path
    except Exception as e:
        pass
        # load default configuration file as re-load failed
        # display configuration
        # ask if edit
        # edit: open new menu to edit configuration
        # save: save configuration and continue

def clear():
    # clear the console
    pass


def main():
    # log application start : start_log
    # load configurations  : load_config
    # start program by loading initial menu
    # log application end : stop_log
    config = get_default_configs()
    print(str(config))

    pass


if __name__ == '__main__':
    main()

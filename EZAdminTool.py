from os import system, name


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
        if selection in range(0, len(menu_options)):
            list(menu_options.values())[int(selection)]()
            clear()
        elif selection.lower() == 'q':
            break
    clear()

def ad_management():
    title = "AD Management"
    pass


def reports():
    title = "Reports"
    pass


def main_configuration():
    title = "Configuration"
    pass


def main_menu():
    title = "EZAdmin Tool"
    menu_options = {'AD Management': ad_management, 'Reports': reports, 'Configuration': main_configuration}
    show_menu(title, menu_options)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    main_menu()
    pass


if __name__ == '__main__':
    main()

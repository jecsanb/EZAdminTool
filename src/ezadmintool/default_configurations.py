APP_NAME = 'EZAdminTool'
CONFIG_FILE_NAME = f'{APP_NAME}.config.txt'
DEFAULT_CONFIG_PATH = './' + CONFIG_FILE_NAME
DEFAULT_TEXT_EDITORS = {'Linux': 'gedit', 'Windows': 'notepad.exe'}
DEFAULT_CONFIG_STRING = \
    """
    # Configuration file for EZAdmin tool.
    [EZADMIN]
    # Set to True once updated with correct settings.
    CONFIGURED : False
    CONFIG_PATH : ./EZAdminTool.config.txt

    [SERVER]
    # Server accepts IP Address or FQDN assuming DNS can resolve and default to default LDAP port.
    HOST_NAME : sample_server
    PORT : 389

    [LDAP_SEARCH_PATHS]
    # The organization units where to search for users and groups.
    0 : OU=Users,DC=sample,DC=com
    1 : OU=Other,DC=sample,DC=com
    2 : OU=Other2,DC=sample,DC=com

    [AUTHENTICATION]
    # Used to authenticate to the directory server
    AUTHENTICATION_DOMAIN : sample.com
    USERNAME : sample
    PASSWORD : password"""

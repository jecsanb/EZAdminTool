from enum import Enum

from ldap3 import Server, Connection, ALL
from ldap3.utils.conv import escape_filter_chars

from ezadmintool.config_management import ConfigurationManagement


class Entity:
    def delete(self):
        pass

    def rename(self):
        pass

    def relocate(self, container_path):
        pass

    def member_of(self):
        pass

    def copy(self):
        pass


class User(Entity):
    __GENERAL_ATTRIBUTES = {
        'givenName': 'First Name',
        'initials': 'Initials',
        'sn': 'Last Name',
        'displayName': 'Display Name',
        'description': 'Description',
        'physicalDeliveryOfficeName': 'Office',
        'telephoneNumber': 'Telephone Number',
        'mail': 'Email Address',
        'wWWHomePage': 'Web Page',
        'CN': 'Common Name',
    }

    @staticmethod
    def general_attributes(include_friendly_name=False):
        return list(User.__GENERAL_ATTRIBUTES if include_friendly_name else User.__GENERAL_ATTRIBUTES.keys())

    def lock(self):
        pass

    def unlock(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def reset_password(self):
        pass


class Group(Entity):
    def add(self):
        pass

    def remove(self):
        pass

    def members(self):
        pass

    pass

    @classmethod
    def general_attributes(cls):
        pass


class ADConfiguration:

    def __init__(self, config=None):
        self.HOST_NAME = None
        self.PORT = None
        self.USERNAME = None
        self.PASSWORD = None
        if config is None:
            config = dict()
        self.required = ['host_name']
        self.optional = ['port', 'username', 'port', 'password']
        for attribute in (self.required + self.optional):
            if attribute in self.required and attribute not in config:
                raise ValueError(f'Missing attribute : {attribute}')
            setattr(self, attribute.upper(), config[attribute] if attribute in config else None)
        self.correct_types()

    def correct_types(self):
        self.PORT = int(self.PORT)

    def __str__(self):
        str = ''
        for attribute in (self.required + self.optional):
            str += f'{attribute} : {getattr(self, attribute, "")}\n'
        return str


class ADConnection:
    def __init__(self, config):
        self.server = Server(host=config.HOST_NAME, port=config.PORT, get_info=ALL)
        self.connection = Connection(self.server, user=config.USERNAME, password=config.PASSWORD)
        self.connected = False

    def search(self, base=None, filter_string='(objectClass=*)'):
        return self.connection.search(base, filter_string)

    def connect(self):
        self.connected = self.connection.bind()

    def disconnect(self):
        self.connected = not self.connection.unbind()

    def test_connection(self):
        self.connect()
        connected = self.connected
        self.disconnect()
        return connected


class ActiveDirectory:
    def __init__(self, config):
        self.config = ADConfiguration(config)
        self.connection = ADConnection(self.config)
        self.connection.connect()

    class SearchType(Enum):
        USER = 0
        GROUP = 1
        ALL = 2

    def add(self, entity, copy=None, container_path=None, template=None):
        pass

    def user_search_filter(self):
        return

    def find(self, name, search_type=ALL):
        attributes = None
        if search_type == self.SearchType.USER:
            search_filter = self.SearchFilter.user_search_filter(name)
            attributes = User.general_attributes()
        elif search_type == self.SearchType.GROUP:
            search_filter = self.SearchFilter.group_search_filter(name)
            attributes = Group.general_attributes()
        else:
            search_filter = self.SearchFilter.all_search_filter(name)
        self.connection.connection.search(self.connection.server.info.naming_contexts[0], search_filter,
                                          attributes=attributes)
        return self.connection.connection.entries

    class SearchFilter:
        @classmethod
        def user_search_filter(cls, name):
            return '(&(objectClass=user)(|(userPrincipalName={0})(sAMAccountName={0})(uid={0})(mail={0})' \
                   '(distinguishedName={0})(proxyAddresses=SMTP:{0})))'.format(
                escape_filter_chars(name))

        @classmethod
        def group_search_filter(cls, name):
            return '(&(objectClass=Group)(|(cn={0})(distinguishedName={0})))'.format(
                escape_filter_chars(name))

        @classmethod
        def all_search_filter(cls, name):
            return '(&(objectClass=*)(cn:={0}))'.format(
                escape_filter_chars(name))


def main():
    configurations = ConfigurationManagement()
    server_conf = dict(configurations.active_configs['SERVER'])
    auth_conf = dict(configurations.active_configs['AUTHENTICATION'])
    ad = ActiveDirectory({**server_conf, **auth_conf})
    result = ad.find('Cert Publishers')
    print(result)


if __name__ == '__main__':
    main()

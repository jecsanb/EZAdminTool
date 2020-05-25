from ldap3 import Server, Connection, ALL


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


class ADConfiguration:
    def __init__(self, config=None):
        self.HOST_NAME = None
        self.PORT = None
        self.USERNAME = None
        self.PASSWORD = None

        if config is None:
            config = dict()
        self.required = ['HOST_NAME']
        self.optional = ['PORT', 'USERNAME', 'PORT']
        for attribute in (self.required + self.optional):
            if attribute in self.required and attribute not in config:
                raise ValueError(f"Missing attribute : {attribute}")
            setattr(self, attribute, config[attribute] if attribute in config else None)

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

    pass

    def add_entity(self, entity, copy=None, container_path=None, template=None):
        pass

    def find_entity(self):
        pass

def main():
    config = ADConfiguration({'HOST_NAME': 'AD_001'})
    print(config)


if __name__ == '__main__':
    main()

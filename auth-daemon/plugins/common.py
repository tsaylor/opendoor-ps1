class BasePlugin():
    def __init__(self):
        pass

    def authenticate(self, jCard):
        return False

    def authorize(self, jCard, resource):
        return False

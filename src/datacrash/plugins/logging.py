from datacrash import Plugin


class LoggerPlugin(Plugin):
    """example plugin that logs the instance only if the fields change

    Args:
        Plugin (_type_): _description_
    """

    def __init__(self, print_fn: callable = None, prefix: str = "DATAcrash"):
        self.print = print_fn or self.print

    def print(self, *args, **kwargs):
        print(*args, **kwargs)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            if self.__dict__[name] != value:
                self.print(f"changed {name} from {self.__dict__[name]} to {value}")
        else:
            self.print(f"set {name} to {value}")
        self.__dict__[name] = value

from dataclasses import is_dataclass

from datacrash.plugin import Plugin


def datacrash(plugins: list[Plugin]):
    plugins = plugins if isinstance(plugins, (list, tuple)) else [plugins]

    def outer_wrapper(cls):
        if not is_dataclass(cls):
            raise TypeError("datacrash can only be applied to dataclasses")

        for plugin in plugins:
            cls = plugin.hook(cls)

        return cls

    return outer_wrapper

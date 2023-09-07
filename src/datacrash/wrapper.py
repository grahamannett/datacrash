from dataclasses import is_dataclass

from functools import wraps
from datacrash.plugin import Plugin


# wrapper for dataclasses,
# possible will want @wraps(cls) to preserve the original class name, e.g.
# @wraps(cls)
# def wrapper(cls):
#     for plugin in plugins:


def datacrash(plugins: list[Plugin]):
    plugins = plugins if isinstance(plugins, list) else [plugins]

    def outer_wrapper(cls):
        if not is_dataclass(cls):
            raise TypeError("datacrash can only be applied to dataclasses")

        for plugin in plugins:
            cls = plugin.process(cls)
        return cls

    return outer_wrapper

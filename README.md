# datacrash

the point of this module is to make something as understandable and chill as dataclasses extremely cringe and awful.
it provides a decorator that wraps around standard dataclasses, allowing for automatic data storage without altering the original data or its behavior.

# features
- transparent integration: use datacrash with your existing dataclasses without any modifications to the actual data. (not sure if this is true tbh)
- extensible: extend dataclasses to be logged/stored/etc with anything

## Basic Usage

```python
from dataclasses import dataclass
from datacrash import datacrash
from datacrash.plugins.tinydb import TinydbPlugin

tinydb_plugin = TinydbPlugin(db_path="output/db.json")

@datacrash(plugins=tinydb_plugin)
@dataclass
class MyDataClass:
    name: str
    price: float
```
with above, now every instance of MyDataClass will automatically be persisted in a TinyDB database located at output/db.json.

# extending datacrash
datacrash is designed with extensibility in mind. You can easily create plugins to support other storage backends:

create a new plugin: the plugin class should inherit from the base plugin class provided by datacrash as the hooks will be more defined later.
implement required rethods: depending on the storage backend, you might need to override methods like hook, on_init, and on_change.

using the 🔌: Once your plugin is ready, simply pass it to the datacrash decorator to start using it.
for more details on creating plugins, refer to the provided TinydbPlugin as an example.

The `hooks` might change as its unclear to me best way to modify the classes that `@dataclass` wraps (ideally would use `__post_init__` but dont think that is feasible)
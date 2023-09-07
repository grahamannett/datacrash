import tinydb

from datacrash.plugin import Plugin


class defaultDb(tinydb.TinyDB):
    def __init__(self, db_file: str):
        super().__init__(db_file)


class tinydbPlugin(Plugin):
    tinydb = tinydb

    def __init__(self, db: tinydb.TinyDB = None, db_path: str = None):
        self.db = db or defaultDb(db_path)

    def process(self, dataclass):
        table = self.db.table(dataclass.__name__)

        original_init = dataclass.__init__

        def _init(instance, *args, **kwargs):
            original_init(instance, *args, **kwargs)
            table.insert(instance.__dict__)

        dataclass.__init__ = _init
        dataclass.table = table

        return dataclass

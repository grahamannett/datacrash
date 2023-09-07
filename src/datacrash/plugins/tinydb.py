from tinydb import TinyDB, table
from dataclasses import asdict
from datacrash.plugin import Plugin


class DefaultDb(TinyDB):
    def __init__(self, db_file: str):
        super().__init__(db_file)


class TinydbPlugin(Plugin):
    def __init__(self, db: TinyDB = None, db_path: str = None):
        self.db = db or DefaultDb(db_path)

    def hook(self, dataclass):
        """Hooks the dataclass to the database."""
        dataclass.table = self.db.table(dataclass.__name__)

        self._on_init(dataclass)
        self._on_change(dataclass)

        return dataclass

    def _on_init(self, dataclass):
        """Modify the dataclass's __init__ to insert into the database."""
        orig_init = dataclass.__init__

        def new_init(instance, *args, **kwargs):
            orig_init(instance, *args, **kwargs)
            instance._doc_id = dataclass.table.insert(asdict(instance))

        dataclass.__init__ = new_init

    def _on_change(self, dataclass):
        """Modify the dataclass's __setattr__ to update the database."""
        orig_setattr = dataclass.__setattr__

        def new_setattr(instance, name, value):
            orig_setattr(instance, name, value)

            if hasattr(instance, "_doc_id"):
                doc = table.Document(asdict(instance), doc_id=instance._doc_id)
                dataclass.table.upsert(doc)

        dataclass.__setattr__ = new_setattr

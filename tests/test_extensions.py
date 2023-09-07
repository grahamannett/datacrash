import unittest
from dataclasses import dataclass

from datacrash import datacrash
from datacrash.plugins.tinydb import tinydbPlugin

tinydb = tinydbPlugin(db_path="output/db.json")


@dataclass
class DataclassItem:
    name: str
    price: float


@datacrash(plugins=tinydb)
@dataclass
class DatacrashItem:
    name: str
    price: float


class TestExtension(unittest.TestCase):
    def test_tinydb(self):
        item = DataclassItem(name="test", price=1.0)
        item_dc = DatacrashItem(name="test", price=1.0)
        assert item.name == item_dc.name
        assert len(DatacrashItem.table) != 0

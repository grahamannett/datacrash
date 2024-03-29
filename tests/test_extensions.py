import unittest
from dataclasses import dataclass

from datacrash import datacrash
from datacrash.plugins.tinydb import TinyDB_Plugin

tinydb = TinyDB_Plugin(db_path="output/db.json")


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
    def setUp(self):
        tinydb.db.drop_tables()

    def test_dataclass_item_creation(self):
        item = DataclassItem(name="test", price=1.0)
        item_dc = DatacrashItem(name="test", price=1.0)

        self.assertEqual(item.name, item_dc.name)
        self.assertEqual(item.price, item_dc.price)

    def test_datacrash_item_insertion(self):
        item_dc = DatacrashItem(name="test", price=1.0)
        self.assertEqual(len(DatacrashItem.table), 1)

    def test_datacrash_item_modification(self):
        item_dc = DatacrashItem(name="test", price=1.0)
        item_dc.name = "modified_name"

        self.assertEqual(len(DatacrashItem.table), 1)
        modified_item = DatacrashItem.table.get(doc_id=item_dc._doc_id)
        self.assertEqual(modified_item["name"], "modified_name")

    # Additional tests
    def test_datacrash_item_multiple_insertions(self):
        items = [DatacrashItem(name=f"test_{i}", price=1.0) for i in range(5)]
        self.assertEqual(len(DatacrashItem.table), 5)

    def test_datacrash_item_deletion(self):
        item_dc = DatacrashItem(name="test", price=1.0)
        DatacrashItem.table.remove(doc_ids=[item_dc._doc_id])
        self.assertEqual(len(DatacrashItem.table), 0)

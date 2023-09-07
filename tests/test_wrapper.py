import unittest

# from dataclasses import dataclass

from datacrash import dataclass
from datacrash.extensions.tinydb import tinydbExtension


@dataclass
class Table:
    name: str
    vals: list


datacrashwrapper = tinydbExtension(db_file="test.json")


@dataclass
class TableExt:
    pass


class TestWrapper(unittest.TestCase):
    def test_wrapper(self):
        t = Table("test", [1, 2, 3])
        self.assertEqual(t.name, "test")
        self.assertEqual(t.vals, [1, 2, 3])
        breakpoint()

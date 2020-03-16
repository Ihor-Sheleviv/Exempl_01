import unittest
from exempl import exempl


class TestLoadData(unittest.TestCase):
    def test_load_one_goods(self):
        self.assertEqual(exempl(), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest
import lib

class TestLib(unittest.TestCase):
    def test_find_waldo(self):
        self.assertEqual(lib.find_waldo("hello"), "not here")
        self.assertEqual(lib.find_waldo("hello waldo"), "here")
        self.assertEqual(lib.find_waldo("hewaldollo"), "here")
        self.assertEqual(lib.find_waldo("Hello Waldo"), "here")
        self.assertEqual(lib.find_waldo("HELLO WALDO"), "here")
        self.assertEqual(lib.find_waldo("HEWALDOLLO"), "here")
        self.assertEqual(lib.find_waldo("w a l d o"), "not here")

if __name__=="__main__":
    unittest.main()

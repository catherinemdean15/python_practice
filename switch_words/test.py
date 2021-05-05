import unittest
import lib

class TestLib(unittest.TestCase):
    def test_switch_words(self):
        self.assertEqual(lib.switch_words("Golden Bear"), "Bear Golden")
        self.assertEqual(lib.switch_words("day snow"), "snow day")
        self.assertEqual(lib.switch_words("cats dogs"), "dogs cats")
        self.assertEqual(lib.switch_words("science computer"), "computer science")

if __name__=="__main__":
    unittest.main()

import unittest
import lib

class TestLib(unittest.TestCase):
    def test_replace_like(self):
        self.assertEqual(lib.replace_like("I like recess"), "I dislike recess")
        self.assertEqual(lib.replace_like("I like computer science"), "I love computer science")
        self.assertEqual(lib.replace_like("I like broccoli"), "I dislike broccoli")
        self.assertEqual(lib.replace_like("I like coding computers"), "I love coding computers")

if __name__=="__main__":
    unittest.main()

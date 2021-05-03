import unittest
import practice

class TestLib(unittest.TestCase):
    def test_remove_last_e(self):
        self.assertEqual(practice.remove_last_e("ma"), "ma")
        self.assertEqual(practice.remove_last_e("mee"), "me")
        self.assertEqual(practice.remove_last_e("ee"), "e")
        self.assertEqual(practice.remove_last_e("made"), "made")
        self.assertEqual(practice.remove_last_e("merry"), "merry")
        self.assertEqual(practice.remove_last_e("pleasee"), "please")

if __name__=="__main__":
    unittest.main()

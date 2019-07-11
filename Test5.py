from io import StringIO
import unittest
from unittest.mock import patch
from P5 import ForTheString

print("To test please input 'yes'")
gs = ForTheString()
gs.getString()
class TestForTheString(unittest.TestCase):
    def test_getString(self):
        self.assertEqual(gs.s, 'yes')

    @patch('sys.stdout', new_callable=StringIO)
    def test_printSTring(self, output_s):
        gs.printString()
        self.assertEqual("YES\n", output_s.getvalue())


if __name__ == "__main__":
    unittest.main()

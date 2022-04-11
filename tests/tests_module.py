import unittest

from  mypackage.module import tiny


class TestCore(unittest.TestCase):

    def test_tiny(self):
        """
        Test that tiny returns the parameter it receives
        """
        self.assertEqual(tiny(1), 1)


if __name__ == '__main__':
    unittest.main()

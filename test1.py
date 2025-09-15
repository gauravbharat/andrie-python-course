import unittest
import ut_source


class TestGuess(unittest.TestCase):
    def test_input(self):
        result = ut_source.run_guess(5, 5)
        self.assertTrue(result)

    def test_input2(self):
        result = ut_source.run_guess(5, 0)
        self.assertTrue(result is None)

    def test_input3(self):
        result = ut_source.run_guess(12, 0)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

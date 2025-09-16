import unittest
import JPGtoPNGconvertor


class TestConversion(unittest.TestCase):
    def test_success(self):
        result = JPGtoPNGconvertor.conversion('Pokedex', 'converted2')
        self.assertTrue(result)

    def test_no_folder(self):
        result = JPGtoPNGconvertor.conversion('okedex', 'converted2')
        self.assertFalse(result)

    def test_no_files_to_convert(self):
        result = JPGtoPNGconvertor.conversion('converted2', 'converted')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
import unittest
import merge_pdf


class TestPdfOperations(unittest.TestCase):
    def test_no_file_exist(self):
        result = merge_pdf.merge(['report.pdf', 'manual.pdf'])
        self.assertFalse(result)

    def test_invalid_file_names(self):
        result = merge_pdf.merge(["document1.txt", "report.pdf", "image.jpg", "manual.pdf", "invalid"])
        self.assertFalse(result)

    def test_only_one_pdf_file(self):
        result = merge_pdf.merge(["dummy.pdf"])
        self.assertFalse(result)

    def test_merge_success(self):
        result = merge_pdf.merge(["dummy.pdf", "twopage.pdf", "wtr.pdf"])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()


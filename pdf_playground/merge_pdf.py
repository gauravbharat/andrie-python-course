import sys
from pypdf import PdfWriter
from pdf_util import validate_pdf_filenames


def merge(pdf_list):
    try:
        ret_val = validate_pdf_filenames(pdf_list, 2)

        if ret_val['validated']:
            merge_file_name = 'merged-pdf.pdf'
            merger = PdfWriter()
            for pdf in ret_val['pdf_file_names']:
                merger.append(pdf)
            merger.write(merge_file_name)
            merger.close()
            print(f'Files merged and saved as {merge_file_name}\n')
            return True
        else:
            return False
    except Exception as e:
        print(f'Error occurred merging pdf files: {pdf_list}\n'
              f'Error: {e}\n')
        return False


if __name__ == '__main__':
    try:
        print('---------')
        print('MERGE')
        print('---------')
        inputs = sys.argv[1:]
        merge(inputs)
        print('*** End of program ***')
    except Exception as e:
        print(f'Error: {e}')



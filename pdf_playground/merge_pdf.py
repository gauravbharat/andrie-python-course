import sys
from pathlib import Path
from pypdf import PdfWriter


def merge(pdf_list):
    try:
        current_directory = Path.cwd()
        pdf_file_names = [f for f in pdf_list if f.endswith('.pdf')
                          and Path.exists(current_directory / f)]
        total_pdf = len(pdf_file_names)

        print('PDF files to merge that exists in current dir: ', pdf_file_names)
        print('----------------------------------------------------------------')

        if not pdf_file_names or total_pdf < 2:
            print(f'You need to pass existing pdf file names to merge from the current directory like:\n'
                  f'python3 script_file_name.py <file1.pdf> <file2.pdf> <fileN>.pdf\n')
            return False
        else:
            merge_file_name = 'merged-pdf.pdf'

            merger = PdfWriter()
            for pdf in pdf_file_names:
                merger.append(pdf)
            merger.write(merge_file_name)
            merger.close()
            print(f'Files merged and saved as {merge_file_name}\n')
            return True

    except Exception as e:
        print(f'Error occurred merging pdf files: {pdf_list}\n'
              f'Error: {e}\n')
        return False


if __name__ == '__main__':
    try:
        inputs = sys.argv[1:]
        merge(inputs)

    except Exception as e:
        print(f'Error: {e}')



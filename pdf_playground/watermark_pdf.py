import sys
from pdf_util import validate_pdf_filenames
from pypdf import  PdfWriter, PdfReader


def watermark(pdf_list):
    try:
        ret_val = validate_pdf_filenames(pdf_list)

        if ret_val['validated']:
            stamp = PdfReader("wtr.pdf").pages[0]
            for pdf_file_name in ret_val['pdf_file_names']:
                writer = PdfWriter(clone_from=pdf_file_name)
                for page in writer.pages:
                    page.merge_page(stamp, over=False)  # here set to False for watermarking
                new_file_name = 'wtr_' + pdf_file_name
                writer.write(new_file_name)
                print(f'Watermarked {pdf_file_name} => {new_file_name}')
            return True
        else:
            return False
    except Exception as e:
        print(f'Error occurred watermarking pdf files: {pdf_list}\n'
              f'Error: {e}\n')
        return False


if __name__ == '__main__':
    try:
        print('---------')
        print('WATERMARK')
        print('---------')
        inputs = sys.argv[1:]
        watermark(inputs)
        print('*** End of program ***')
    except Exception as e:
        print(f'Error: {e}')
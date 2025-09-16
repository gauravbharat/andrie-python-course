from pathlib import Path


def validate_pdf_filenames(pdf_list, min_files=1):
    ret_val = {
        'pdf_file_names': [],
        'validated': False
    }

    try:
        current_directory = Path.cwd()
        ret_val['pdf_file_names'] = [f for f in pdf_list if f.endswith('.pdf')
                                     and Path.exists(current_directory / f)]
        total = len(ret_val['pdf_file_names'])

        print('PDF files that exists in current dir: ', ret_val['pdf_file_names'])
        print('----------------------------------------------------------------')

        if not ret_val['pdf_file_names'] or total < min_files:
            print(f'You need to pass existing pdf file names from the current directory like:\n'
                  f'python3 script_file_name.py <file1.pdf> <file2.pdf> <fileN>.pdf\n')
        else:
            ret_val['validated'] = True

    except Exception as e:
        print(f'Error validating pdf file names: {pdf_list}\n'
              f'Error: {e}')
    finally:
        return ret_val

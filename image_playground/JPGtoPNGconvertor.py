from pathlib import Path
from PIL import Image
import os


def conversion(folder_name, destination_folder_name, search_path="."):
    try:
        """Search for folder in current directory only"""
        search_directory = Path(search_path)

        folder_found = False
        for item in search_directory.iterdir():
            if item.is_dir() and item.name == folder_name:
                folder_found = True

                if not os.path.exists(destination_folder_name):
                    os.makedirs(destination_folder_name)

                # print(f"Found folder: {item}")
                is_jpeg_exists = bool(list(item.glob("*.jpg"))) or bool(list(item.glob("*.jpeg")))

                if is_jpeg_exists:
                    # Create Path object for the folder
                    destination_folder_path = Path(destination_folder_name)

                    # # Create the folder if it doesn't exist
                    # destination_folder_path.mkdir(parents=True, exist_ok=True)

                    # Loop through files
                    for file_path in item.iterdir():
                        if file_path.is_file() and (file_path.match('*.jpg') or file_path.match('*.jpeg')):
                            try:
                                print(f"  Converting {file_path.name}...")

                                # Create full file path
                                destination_file_path = f'{destination_folder_path}/{file_path.stem}.png'
                                # print(destination_file_path)
                                img = Image.open(file_path)
                                img.save(destination_file_path, 'png', compress_level=6, optimize=True, )
                                print(f"  Conversion completed: {destination_file_path}")
                            except Exception as e:
                                print(f"Error converting {file_path.name}\n{e}")
                    return True
                else:
                    print(f'No JPG files found to convert in {folder_name}!')
                    return False
        if not folder_found:
            print(f'No folder name found as {folder_name}!')
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


# Usage
if __name__ == '__main__':
    import sys
    script_file_name = sys.argv[0]

    try:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]

        # print(source_directory, destination_directory)
        conversion(source_directory, destination_directory)
    except IndexError:
        print(f'You need to pass the source and target directory names like:\n'
              f'python3 {script_file_name} <source_directory> <destination_directory>')
    except Exception as e:
        print(f'System error: {e}')




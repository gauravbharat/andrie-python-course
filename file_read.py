
from translate import Translator
translator = Translator(to_lang="pt")
filename = 'test.txt'
save_to_file = 'translated.txt'

try:
    with open(filename, mode='r') as my_file:
        # print(my_file.read())
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)

        with open(save_to_file, mode='a') as my_translations:
            my_translations.write(translation + '\n')
except FileNotFoundError:
    print(f'{filename} does not exist!')
except IOError as io_error:
    print(f'IO Error occurred reading translation file {filename}\nerror: {io_error}')

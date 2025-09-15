from sys import argv
from math import ceil
from custom_exceptions import IndexValuesException, IncorrectInputException
from random import randint

# print(sys.argv, __name__)
try:
    start = ceil(float(argv[1]))
    end = ceil(float(argv[2]))

    # print(start, end)

    if start >= end:
        raise IndexValuesException('Incorrect indexes!', start, end)

    random_integer = randint(start, end)
    # print(f'random_integer: {random_integer}')

    try:
        tries = 0
        while True:
            prompt_message = f'Enter a random number between {start} and {end}: '
            if tries > 0:
                prompt_message = f' Try again, enter a random number between {start} and {end}: '
            user_guess = ceil(float(input(prompt_message)))

            if user_guess == random_integer:
                print('Yeah boy, you guessed it right!!')
                break
            else:
                tries += 1
                continue

    except ValueError:
        raise IncorrectInputException('Incorrect input!', int)

except (ValueError, IndexError):
    print('You need to enter the start and end indexes as integers!')
except IndexValuesException as err:
    print(f'Start index {err.start()} should be less than End index {err.end()}!')
except IncorrectInputException as input_error:
    print(f'Incorrect input for guess number. Expected type is {input_error.expected_type().__name__}')
# except:
#     print('Unknown system error!!')
finally:
    print('*** end of program ***')

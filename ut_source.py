from random import randint
import sys


def run_guess(g, a):
    if 0 < g < 11:
        if g == a:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return  False


# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if run_guess(guess,answer):
                break
        except ValueError:
            print('please enter a number')
            continue

"""Check password strength and whether pwn"""
import sys
from zxcvbn import zxcvbn
import hashlib
import requests


def get_pwd_strength(password):
    result = zxcvbn(password)
    return {
        'score': result['score'],  # 0-4 (0=weak, 4=strong)
        'crack_time': result['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        'feedback': result['feedback']['suggestions'],
        'warning': result['feedback']['warning'],
        'guesses': result['guesses']
    }


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    try:
        if not args:
            print('No passwords to check for!!')

        for idx, password in enumerate(args):
            print(f"\nPassword {idx + 1}: {password}")
            result = get_pwd_strength(password)

            print_strength_result = f'--- Strength results ---'
            print_strength_result += f'\nScore: {result["score"]}; range 0-4 (0=weak, 4=strong)'
            print_strength_result += f'\nApprox. crack time: {result["crack_time"]}'

            if result['feedback']:
                feedbacks = ''.join(f"\n - {item}" for item in result['feedback'])
                print_strength_result += f"\nFeedback/s: {feedbacks}"

            if result['warning']:
                print_strength_result += f'\nWarning: {result["warning"]}'

            print(print_strength_result)

            count = pwned_api_check(password)
            print_pwn_result = f'--- Pwned results ---'
            print(print_pwn_result)
            if count:
                print(f'{password} was found {count} times... you should probably consider another password!')
            else:
                print(f'{password} was NOT found, carry on! However, check password strength results above!!')
    except Exception as e:
        print(f"Error occurred checking password: {e}")
    finally:
        return '\n*** End of program ***'


if __name__ == '__main__':
    print('---------------------')
    print('PASSWORD CHECKER')
    print('---------------------')
    sys.exit(main(sys.argv[1:]))
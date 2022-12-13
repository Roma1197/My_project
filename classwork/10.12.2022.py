import string
import random
flag_num = int(input('Which length of password would you want? (4-16)\n'))
flag_low = input('Would you like to use low register? (y/n)\n').lower()
flag_upp = input('Would you like to use uppercase? (Y/N)\n').upper()
numbers = input('Would you like to use numbers? (y/n)\n').lower()
symbl = input('Would you like to use a symbols? (y/n)\n').lower()
def password_gen():
    '''generate a random password using user input'''
    password_alphabet = ''
    for char in flag_low:
        if flag_low == 'y':
            password_alphabet += string.ascii_lowercase
            break
        elif flag_low == 'n':
            break
        else:
            print('Wrong input, try one more time')
    for char in flag_upp:
        if flag_upp == 'Y':
            password_alphabet += string.ascii_uppercase
            break
        elif flag_upp == 'N':
            break
        else:
            print('Wrong input, try one more time')
    for char in numbers:
        if numbers == 'y':
            password_alphabet += string.digits
            break
        elif numbers == 'n':
            break
        else:
            print('Wrong input, try one more time')
    for char in symbl:
        if symbl == 'y':
            password_alphabet += string.punctuation
            break
        elif symbl == 'n':
            break
        else:
            print('Wrong input, try one more time')
    password_final = []
    for flag in range(flag_num):
        password_symbols = random.choice(password_alphabet)
        password_final.append(password_symbols)
    password = ''.join(password_final)
    print(f"Your password is: {password}")
password_gen()

while True:
    char_list = random.choices(string.ascii_lowercase)
    char_list.append(random.choices(string.ascii_uppercase))
    char_list.append(random.choices(string.digits))
    char_list.append(random.choices(string.punctuation))
    broken_password = random.choince(char_list)
    print()


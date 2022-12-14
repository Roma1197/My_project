import string
import random
import time
flag_num = int(input('Which length of password would you want? (4-8)\n'))
numbers = input('Would you like to use numbers? (y/n)\n').lower()
password_alphabet = ''
for char in numbers:
    if numbers == 'y':
        password_alphabet += string.digits
        break
    elif numbers == 'n':
        break
    else:
        print('Wrong input, try one more time')
password_final = []
for flag in range(flag_num):
    password_symbols = random.choice(password_alphabet)
    password_final.append(password_symbols)
password = ''.join(password_final)
print(f"Your password is: {password}")

def time_counter(f):
    '''Time counter'''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + ' time taken ' + str((end - start)*1000) + ' ms')
        return result
    return wrapper

@time_counter
def password_break(i):
    '''Cracks the password generated above'''
    for i in range(1, 10):
        if i == char:
            break

for n in range(0, len(password)):
    char = int(password[n])
    print(f"{char}")

correct_password = password_break(char)
print(correct_password)

'''create an app in python that will generate standard passwords randomly and unique each time.'''

import random
import string
def random_password():

    characters = string.ascii_letters + string.digits + string.punctuation
    length =int(input("Enter the length of password: "))
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    print("Generated Password: ",random_password())
    
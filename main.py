# import choice from random
from random import choice


# Password Generator Class
class Generator:
    # Creating var with chars
    chars = '!#%*&-_+=@/[];:qwertyuiopasdfghjklzxcvbnm<>,.\'QWERTYUIOPASDFGHJKLZXCVBNM'
    # Password amount and pass length inputs
    amount = int(input('Enter password amount: \n'))
    length = int(input('Enter password length: \n'))

    # Pass generator
    for n in range(amount):
        # Creating password variable
        password = ''
        # Calling password length var.
        for i in range(length):
            # Adds character to var. password
            password += choice(chars)
        print(password)

from pwinput import pwinput
import logging
from typing import Union, Any
logger = logging.getLogger(__name__)

EMPTY_STRING = ''
FILENAME_2 = 'details'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[]{};:.<>/?|~`'
MAX_LENGTH = len(SYMBOLS)

def login() -> bool:
    """
    Prompts the user to enter credentials and compares them with encrypted versions in the file details.txt
    Returns a boolean value True or False depending on if the values match or not

    :return: The bool that depends on the entered credentials and the encrypted credentials and if they match
    """
    user = EMPTY_STRING
    word = EMPTY_STRING
    done = 0
    username = input('Enter username: ')
    password = pwinput('Enter password: ', '*')
    with open(FILENAME_2 + '.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(',')
            user = decrypt_username(line[0]) # decrypts the username in the file and checks if it is equal to the inputted username
            if user == username:
                word = decrypt_password(line[1]) # does the same thing with the password
                if word == password:
                    print('Login success')
                    done = 1
                    break
        if done == 0:
            return False
        else:
            return True

def sign_up() -> None:
    """
    Prompts the user to create an account by entering their username and password, encrypting it and storing it in the file details.txt
    """
    logger.info('Attempting signup')
    finish = False
    try:
        with open(FILENAME_2 + '.txt', 'a') as file:
            while not finish:
                username = input('Create a username: ')
                password = pwinput('Enter a password of minimum 8 characters: ', '*')
                if len(password) < 8: # Checking the length of the password
                    logger.info('Length check')
                    print('Password too short')
                else:
                    username, password = encrypt(username, password) # encrypting the details before storing it in the file
                    file.write('\n' + username + ',')
                    file.write(password)
                    print('Signup successful!')
                    finish = True
    except FileNotFoundError:
        logger.error('File not found')
        print('File not found')
    except:
        logger.error('There is something wrong here!')
        print('Error')

def encrypt(pUsername: str, pPassword: str) -> tuple[Union[str, Any], Union[str, Any]]:#
    """
    Encrypts the username and password before storing them in details.txt

    :param pUsername: The user-entered username
    :param pPassword: The user entered password
    :return: A tuple containing the encrypted username and password
    """
    encrypted_username = EMPTY_STRING
    encrypted_password = EMPTY_STRING
    for i in range(len(pUsername)):
        symbol_index = SYMBOLS.find(pUsername[i])
        if symbol_index == -1:
            encrypted_username += pUsername[i]
        else:
            if i % 2 == 0:
                symbol_index += len(pUsername)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                encrypted_username += SYMBOLS[symbol_index]
            else:
                symbol_index -= len(pUsername)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                encrypted_username += SYMBOLS[symbol_index]

    for i in range(len(pPassword)):
        symbol_index = SYMBOLS.find(pPassword[i])
        if symbol_index == -1:
            encrypted_password += pPassword[i]
        else:
            if i % 2 == 0:
                symbol_index -= len(pPassword)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                encrypted_password += SYMBOLS[symbol_index]
            else:
                symbol_index += len(pPassword)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                encrypted_password += SYMBOLS[symbol_index]

    return encrypted_username, encrypted_password

def decrypt_username(pUsername: str) -> str:
    """
    Decrypts the username from details.txt if a user wishes to log in

    :param pUsername: The user-entered username
    :return: The decrypted username obtained from the file
    """
    decrypted_username = EMPTY_STRING
    for i in range(len(pUsername)):
        symbol_index = SYMBOLS.find(pUsername[i])
        if symbol_index == -1:
            decrypted_username += pUsername[i]
        else:
            if i % 2 == 0:
                symbol_index -= len(pUsername)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                decrypted_username += SYMBOLS[symbol_index]
            else:
                symbol_index += len(pUsername)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                decrypted_username += SYMBOLS[symbol_index]

    return decrypted_username

def decrypt_password(pPassword: str) -> str:
    """
    Decrypts the password from details.txt if a user wishes to log in

    :param pPassword: The user-entered password
    :return: The decrypted password obtained from the file
    """
    decrypted_password = EMPTY_STRING
    for i in range(len(pPassword)):
        symbol_index = SYMBOLS.find(pPassword[i])
        if symbol_index == -1:
            decrypted_password += pPassword[i]
        else:
            if i % 2 == 0:
                symbol_index += len(pPassword)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                decrypted_password += SYMBOLS[symbol_index]
            else:
                symbol_index -= len(pPassword)
                if symbol_index > MAX_LENGTH:
                    symbol_index -= MAX_LENGTH
                elif symbol_index < 0:
                    symbol_index += MAX_LENGTH
                decrypted_password += SYMBOLS[symbol_index]

    return decrypted_password
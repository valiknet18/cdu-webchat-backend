from base64 import b64encode, b64decode

import random

secret_key = '85vyS5SL1KgNBAZ378W0MZaWxjr842sA'


def generate_user_token():
    alpha = 'asdfghjklqwertyuiopzxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP123456789'

    key = ""
    for i in range(0, 100):
        key += random.choice(alpha)

    return key


def encode_user_token(token):
    salt = b64encode(secret_key.encode('ascii'))

    return b64encode(token.encode('ascii')) + salt


def decode_user_token(token):
    salt = b64encode(secret_key.encode('ascii'))

    token = token.replace(salt.decode('ascii'), '')

    return b64decode(token.encode('ascii'))
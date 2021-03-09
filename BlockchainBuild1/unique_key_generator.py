from hashlib import sha256
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import hashlib
#import random
#import string


def hashit(input):
    hashlib.sha256().update(input)
    hashed_input = hashlib.sha256().digest()
    return hashed_input


def hex_hashit(input):
    hashlib.sha256().update(input)
    hashed_input = hashlib.sha256().hexdigest()
    return hashed_input

#########################################################
# IDEA 3


"""class Keys:
    def random_string(self):
        string_characters = string.ascii_letters + string.digits + string.punctuation
        rand_string = ''.join(random.choice(string_characters) for i in range(100)).encode()
        return rand_string

    def generate_sk(self):
        Keys.random_string(Keys)
        sk = hex_hashit(rand_string)
        return sk

Keys.generate_sk(Keys)"""

# The issue with this method is that we don't know how to create the vk with the sk
# It also seems like there's a lot of moving parts...

#########################################################
# IDEA 2

"""def generate_keys_and_address():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key
    vk = vk.to_der()
    address = hashit(vk)
    return sk, vk, address

def new_user():
    pass"""


# IDEA 1:
# Use a metaclass that creates a new user each time it is instantiated.  Each new user is assigned a UUID to which a sk will then be generated and assigned to
# Then have the keys generated in the class that inherits the user metaclass
# New class structure would be: User (metaclass that creates new user when instantiated), Keys (inherits User class and assigns unique keys to each individual user)

# IDEA 2:
# Have a new_user method in the User class that when called, generates a new user and thus new sk, etc.
# This will hopefully prevent repeating sk's being generated when just the simple User class is being instantiated.
# The hope is that by calling the generate key methods inside the new user method, it will create a new random key each time the new_user method is called.
# We can then add each sk to a list and parse through the list upon each new user being created to prevent duplicate sk's being generated.
# (In actuality, however, it would be better to have the vk's entered into a list so that the sk's wouldn't be able to be seen and hacked)

# IDEA 3:
# Create your own key generator from scratch using randomly generated data strings.

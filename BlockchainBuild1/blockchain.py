from hashlib import sha256
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from ecdsa.util import PRNG
import hashlib
import random
import sys

"""class Blockchain:
    def __init__(self):
        chain = []"""

"""class Block:
    prev_hashcode = 1

    def __init__(self, prev_hashcode, tx_data, nonce, current_hashcode):
        pass

    def tx_data(self):
        pass

    # Semi-random number based on difficulty
    # Modify later when difficulty algo is built
    def nonce(self):
        nonce = random.randint(0, sys.maxsize)
        return nonce

    def current_hashcode(self):"""

def hashit(input):
    hashlib.sha256().update(input)
    hashed_input = hashlib.sha256().digest()
    return hashed_input

#########################################################

class User:
    # Calls the methods to generate sk, vk, address when the class is instantiated
    def __init__(self):
        User.generate_sk(self)
        User.generate_vk(self)
        User.generate_address(self)

    def generate_sk(self):
        self.sk = SigningKey.generate(curve=SECP256k1)
        return self.sk

    def generate_vk(self):
        User.generate_sk(User)
        self.vk = self.sk.verifying_key
        self.vk = self.vk.to_der()
        return self.vk

    def generate_address(self):
        self.address = hashit(self.vk)
        return self.address

user = User()
#user2 = User() #How to make it so it creates a new instance of the class (so it makes new sk, vk, etc.)?
# ^ I don't think the same machine can create different keys... I think it might create new keys for each different machine
# So we might just have to text everything with 2 different computers.  So we would have to set up the network functionability so other people can connect to network.

print(user.address)

#########################################################

"""class Tx(User):
    # Init function, used for each new transaction that is created.
    def __init__(self, sending_address, receiving_address): # Add proof, signature?  Should I add message (or not bc its being created from the inputs)
        self.sending_address = sending_address
        self.receiving_address = receiving_address
        #self.proof = proof
        #self.signature = signature
        Tx.new_transaction(self, sending_address, receiving_address)

        #assert self.vk.verify(self.signature, b"message") # ???

    def new_transaction(self, sending_address, receiving_address): #Add proof, message?, and signature?
        #self.proof = #ENTER PROOF FROM MERKLE TREE
        #self.signature = self.sending_address
        self.tx_message = hashit(self.sending_address + self.receiving_address) #add self.proof
        return self.tx_message

    # Current idea/thought.  Will probably have to make a signature in User class instead and then reference it here.  Bc we can't derive sk from address (we're only given address here)
    def sign(self):
        #sender_sign = self.sending_address.vk
        self.signature = hashit(self.tx_message + self.sending_address.sk)


tx1 = Tx(user1.address, user2.address)

#print(tx1.tx_message)
print(tx1.sending_address.vk)"""

    # The organizational structure/layout of all transactions in a block
    # Returns a merkle root - This is what will be entered/used to help generate current hashcode
    #def merkle_tree(self):
    #    pass


#########################################################

"""    # Input transactions of tx being conducted
    def inputs():
        pass

    # Digests of previous tx's resulting in BTC being sent
    def input_proof():
        pass

    # Who transaction is being sent to 
    def outputs():
        pass

    # Hashed version of entire transaction.  Added to merkle tree as a leaf
    def message():
        pass

    # Merkle tree - Used in organizing transactions, particularly hashed transactions
    def merkle_tree():
        pass
    def merkle_leaf():
        pass
    def merkle_branch():
        pass
    def merkle_root():
        pass


class Mining:
    # Cycles through potential nonces to match hash to goal set by PoW
    def nonce_finder():
        pass"""

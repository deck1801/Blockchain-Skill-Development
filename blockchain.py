# Module-1/Practical-1 Create a Blockchain
import datetime #timestamping the blocks
import hashlib #hasing feature of the blocks
import json #encoding of blocks
from flask import Flask, jsonify #web application itself

# building a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []  #list containig different blocks
        self.create_block(proof=1,previous_hash = '0') #genesis Block
        


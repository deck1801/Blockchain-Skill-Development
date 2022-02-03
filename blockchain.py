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
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 }
        self.chain.append(block)
        return block
        #dictonary with 4 essential elements index,timestamp,proof,prev_hash
    
    def get_previous_block(self):
        return self.chain[-1]
        
    #proof of work is a specific number founded by a miner hard to find and 
    #easy to verify
    
    def proof_of_work(self, previous_proof):
        new_proof=1 #we have to increment this and check wheather it correct
        check_proof=False
        while check_proof is False:
            #problem miner have to solve
            hash_operation=hashlib
        
        


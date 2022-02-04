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
    #easy to verify it is improtant to mine a new block
    
    def proof_of_work(self, previous_proof):
        new_proof=1 #we have to increment this and check wheather it correct
        # we are solving problem with hit & trial method 
        check_proof=False #intaillaly remains False
        while check_proof is False:
            #problem miner have to solve
            #number of zero increases the more tougher it will be to solve the problem
            #proof needed to be asymetrical operation in nature
            hash_operation=hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            #using haslib.sha256 function defining asymetric problem str formate and
            #encoding fucntion to encode function
            #since hashes in blockchain is in hexadecimal so hexdigest()
            if hash_operation[:4]=='0000': #the upper-bound is always excluded
                check_proof=True
            else:
                new_proof += 1;
        return new_proof
    
    def hash(silf,block):
        #This function will give us dedicatred hash of each block an since our 
        #contains data into dictinoary format but will change it to json format and use
        #Json damp function
        encoded_block = json.dumps(block,sort_keys=True).encode() #converted to json
        return hashlib.sha256(encoded_block).hexdigest() #hexadecimal format


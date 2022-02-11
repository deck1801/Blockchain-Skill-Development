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
        #This function will give us dedicated hash of each block and since our block 
        #contains data into dictinoary format but will change it to json format and use
        #Json damp function
        encoded_block = json.dumps(block,sort_keys=True).encode() #converted to json
        return hashlib.sha256(encoded_block).hexdigest() #hexadecimal format
    
    def is_chain_valid(self,chain):
        #This function will check the validation of the chain simple and fast procedure
        previous_block = chain[0] #gensis block  
        block_index = 1 #1st block after gensis block
        while(block_index<len(chain)): #checking the link by verfying the previous hash
            block= chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof=previous_block['proof'] #validating proof of work 
            proof=block['proof']
            hash_operation=hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            #required hash operation
            #checking four leading zeros
            if(hash_operation[:4]!='0000'):
                return False
            previous_block = block #incrementing block
            block_index=block_index+1; #incrementing while loop 
        return True

# Mining of our blockchain
app=Flask(__name__)
app.config['JASONIFY_PRETTYPRINT_REGULAR']=False
blockchain = Blockchain() #very first block chain

@app.route('/mine_block',methods = ['GET']) #routing decorater
def mine_block():
    previous_block=blockchain.get_previous_block()
    previous_proof=previous_block['proof']
    proof=blockchain.proof_of_work(previous_proof)
    previous_hash=blockchain.hash(previous_block)
    block=blockchain.create_block(proof, previous_hash)
    
    response={'message':"Congratulations ,you just mined a block",
              'index':block['index'],
              'timestamp':block['timestamp'],
              'proof': block['proof'],
              'previous_hash':block['previous_hash']
              }
    
    return jsonify(response),200

#getting full blockchain
@app.route('/get_chain',methods = ['GET'])
def get_chain():
    response = {'chain':blockchain.chain,
                'length': len(blockchain.chain),
                }
    return jsonify(response),200

#Running the App

@app.route('/valid_chain',methods = ['GET'])
def vaild_chain():
    if(blockchain.is_chain_valid(blockchain.chain)):
        response={'message':"Chain is successfully verified",}
    
    return jsonify(response),200
app.run(host='0.0.0.0',port=5000)





















 



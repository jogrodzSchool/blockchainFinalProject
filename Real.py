# Amim Mohammad - 100765511
# Donovan Condo - 100752997
# Jordan Grodzinski - 100764753

from Stakeholder import mainstake
from Stakeholder import mainshare

import random
import json
import hashlib
from time import time



class Blockchain():


    def __init__(self):
        self.flag = 1
        self.chain = []
        self.current_transaction = []
        genesis_Hash = self.Hash("genesis_block")
        self.append(
            Previous_block_hash=genesis_Hash,
            nonce=1)


    def Hash(self,i):
        blockEncoder = json.dumps(i, sort_keys=True).encode()
        x = hashlib.sha256(blockEncoder).hexdigest()
        return x

    def append(self,  Previous_block_hash, nonce):
        block = {
            'index': len(self.chain),
            'transactions': self.Smart(), # The data that the Smart contract returns
            'timestamp': time(),
            'nonce': nonce,
            'Previous_block_hash': Previous_block_hash
        }
        self.prev = Previous_block_hash
        self.current_transaction = []
        self.chain.append(block)
        return block

    def PoS(self,nonce,prevhash, data):
        obj1 = mainshare()
        obj2 = mainstake()
        print(obj1)
        x= self.Smart()
        pool=set()

        # Depending on the stakes from obj2 we will determine how much an address wishes to stake.
         # The stakes of the users would be added in a pool. Higher their contribution better the chances of being able to mine the block


        return True or False

    def nonces(self):
        return random.randint(1000,4000)

    def newblock(self):

        scontract = self.flag+1
        x=self.PoS(self.nonces,self.prev,scontract )
        if x == True:
            self.append(self.prev,self.nonces)

         #A Smart Contract will trigger a new creation


    @property
    def last_block(self):
        return self.chain[-1]


    def Smart(self):
        x=random.randint(0,1)
        if x==1:
            return 1
        else:
            return 0
        # This is a Pseudo demo of a smart contract. If the contract triggers positive we accept it into the blockchain.



blk = Blockchain()
blk.PoS(0,0,0)

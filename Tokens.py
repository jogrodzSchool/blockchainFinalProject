import json
import hashlib

class Tokens():
    tok=dict()
    def __init__(self):
        self.tok=dict()

    def token(self, length=500):
        pass

    def append(self):
        for i in range(500):
            blockEncoder = json.dumps(("tok"+str(i)), sort_keys=True).encode()
            x= hashlib.sha256(blockEncoder).hexdigest()
            temp={"tok"+str(i):x}
            self.tok.update(temp)
            for key,value in self.tok.items():
                print(key,value)
        return self.tok

def maintoken():
    token1 = Tokens()
    return token1.append()


maintoken()

import names
from random import randint
from random import sample

import Tokens

class Stakeholder():
    owners = list()
    for i in range(10):
        owners.append(names.get_full_name())
    print(owners)
    ledger=dict()

    def __init__(self):
        self.tok=Tokens.maintoken()       #Contains a dictionary of tokens and their hashes

        self.owners=Stakeholder.owners
        self.ledger=dict()
    def ownership(self):
        return self.owners

    def shares(self):

        self.leger=dict()
        for i in range(10):
            a1 = dict()
            x=self.owners[i]

            a1 = sample(self.tok.items(),randint(1,10))
            # print(a1)
            self.ledger[x] = a1

        return self.ledger


    def stake(self):
        st=list()
        for i in range(10):
            x=randint(0,1)
            if x==0:
                st.append(True)
            else:
                st.append(False)
        return st


def mainstake():
    stakeholder = Stakeholder()
    return stakeholder.stake()

def mainshare():
    stakeholder = Stakeholder()
    return stakeholder.shares()

mainshare()
mainstake()















st=Stakeholder()
x=st.ownership()
print(x)
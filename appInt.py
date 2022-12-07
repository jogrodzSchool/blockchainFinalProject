from tkinter import *
import tkinter as tk
from tkinter import ttk
from Blockchain import Blockchain

class BCFrontEnd(tk.Tk):
    def __init__(self):
        super().__init__()
        #basic settings for the window
        self.title("Welcome to Blockchain Realty!")
        self.geometry("700x600")
        self.resizable(False, False)
        #all the variables for the frontend of the application
        self.bc = Blockchain()
        self.choice = IntVar()
        sAdd = StringVar()
        rAdd = StringVar()
        amount = StringVar()
        self.prevBlock = StringVar()
        #initialize all widgets
        self.r1 = ttk.Radiobutton(
            self,
            text="Buy Property",
            variable=self.choice,
            value=1,
            command=self.buyWindow
        )
        self.r2 = ttk.Radiobutton(
            self,
            text="View Properties",
            variable=self.choice,
            value=2,
            command=self.viewWindow
        )
        self.r3 = ttk.Radiobutton(
            self,
            text="Add New Property Listing",
            variable=self.choice,
            value=3,
            command=self.appendWindow
        )
        self.exit = ttk.Button(
            self,
            text="Exit Application",
            width=20,
            command=self.destroy
        )
        self.submit = ttk.Button(
            self,
            text="Submit",
            width=20,
            command=self.processRequest
        )
        self.sAddLabel = ttk.Label(
            self,
            text="Enter the address for your wallet.",
        )
        self.rAddLabel = ttk.Label(
            self,
            text="Enter the hash of the property token you would like to purchase.",
        )
        self.amtLabel = ttk.Label(
            self,
            text="Enter transfer amount."
        )
        self.sAddr = ttk.Entry(
            self,
            textvariable=sAdd,
        )
        self.rAddr = ttk.Entry(
            self,
            textvariable=rAdd,
        )
        self.amt = ttk.Entry(
            self,
            textvariable=amount
        )
        self.table = ttk.Treeview(
            self,
            column=(
                "User",
                "Total Property Value",
                "Number of Owned Tokens"
            ),
            show="headings",
            height=8
        )
        self.outputSucc = ttk.Label(
            self,
            text="Transaction Successful!"
        )
        self.outputFail = ttk.Label(
            self,
            text="Transaction Failed!"
        )
        self.appendLabel = ttk.Label(
            self,
            text="Enter the address of the blockchain to append to."
        )
        self.blockAddress = ttk.Entry(
            self,
            textvariable=self.prevBlock
        )
        #additonal initialization required for the table that will display blocks in the chain
        self.table.column("# 1", anchor=CENTER)
        self.table.heading("# 1", text="User")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Total Property Value")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Number of Owned Tokens")
        #fixed elements that will not change are displayed
        self.r1.pack(
            anchor=W,
            padx=20,
            pady=10
        )
        self.r2.pack(
            anchor=W,
            padx=20,
            pady=10
        )
        self.r3.pack(
            anchor=W,
            padx=20,
            pady=10
        )
        self.exit.pack(
            anchor=W,
            side="bottom",
            padx=20,
            pady=20,
        )
    #passes the request to the proper function depending on current radio selection
    #after function fires will display if the transaction succeeded or failed
    def processRequest(self):
        if self.choice.get() == 1:
            output = self.bc.Smart()
        elif self.choice.get() == 3:
            output = self.bc.append(999, self.prevBlock)
        if output == True:
            self.outputFail.pack_forget()
            self.outputSucc.pack(
                anchor=CENTER,
                side="bottom",
            )
        else:
            self.outputSucc.pack_forget()
            self.outputFail.pack(
                anchor=CENTER,
                side="bottom",
            )

    #hides all temporary elements, this function is run by each of the three functions tied to the radio
    def cleanUp(self):
        self.sAddLabel.pack_forget()
        self.sAddr.pack_forget()
        self.rAddLabel.pack_forget()
        self.rAddr.pack_forget()
        self.amtLabel.pack_forget()
        self.amt.pack_forget()
        self.submit.pack_forget()
        self.table.pack_forget()
        self.outputSucc.pack_forget()
        self.outputFail.pack_forget()
        self.appendLabel.pack_forget()
        self.blockAddress.pack_forget()

    #displays the elements required in order to purchase property tokens
    def buyWindow(self):
        self.cleanUp()
        self.sAddLabel.pack(
            anchor=CENTER,
            padx=20
        )
        self.sAddr.pack(
            anchor=CENTER,
            padx=20,
            pady=10
        )
        self.rAddLabel.pack(
            anchor=CENTER,
            padx=20
        )
        self.rAddr.pack(
            anchor=CENTER,
            padx=20,
            pady=10
        )
        self.amtLabel.pack(
            anchor=CENTER,
            padx=20
        )
        self.amt.pack(
            anchor=CENTER,
            padx=20,
            pady=10
        )
        self.submit.pack(
            anchor=W,
            side="bottom",
            padx=20,
        )
    #displays a table of user information including total value of all properties owned and the number of property tokens owned
    def viewWindow(self):
        self.cleanUp()
        self.table.pack(
            anchor=CENTER,
            padx=20,
            pady=20
        )
    #displays the elements required to append block
    def appendWindow(self):
        self.cleanUp()
        self.appendLabel.pack(
            anchor=CENTER,
            padx=20,
            pady=10
        )
        self.blockAddress.pack(
            anchor=CENTER,
            padx=20,
            pady=10
        )
        self.submit.pack(
            anchor=W,
            side="bottom",
            padx=20,
        )

if __name__ == '__main__':
    bc = BCFrontEnd()
    bc.mainloop()
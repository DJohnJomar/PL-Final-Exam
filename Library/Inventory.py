'''
The inventory of the program.
Handles both the parts list and transactions list.
The needed modules are imported from the library 
'''
from datetime import datetime
from Library.Transaction import Transaction
class Inventory:

    def __init__(self):
        self.partList = []
        self.transactionList = []

    def addPart(self, part):
        self.partList.append(part)

    #The process of adding a transaction in the list
    def addTransaction(self, condition, part, oldPartNumber):
        currentDate = datetime.now().strftime("%Y-%m-%d")
        error = ""
        transactionDesc = ""

        # Setting Transaction Description
        if condition == 1:
            transactionDesc = "Added a new part"
        elif condition == 2:
            transactionDesc = "Changed description"
        elif condition == 3:
            transactionDesc = "Changed price"
        elif condition == 4:
            transactionDesc = f"Changed part number from: {oldPartNumber}"
        elif condition == 5:
            transactionDesc = "Part Deleted"

        # Setting up the error
        # The errors can be if part number or the part description exceeds the maximum characters.
        # The errors in the transaction disappears if they are fixed accordingly
        if self.checkForError( part):
            if len(str(part.getPartNumber())) > 10 and len(part.getPartDescription()) > 26:
                error = "Part Number and Description EXCEEDS MAXIMUM CHARACTERS (10 and 26 Respectively)."
            elif len(str(part.getPartNumber())) > 10:
                error = "Part Number EXCEEDS THE MAXIMUM CHARACTERS (10)"
            elif len(part.getPartDescription()) > 26:
                error = "Part Description EXCEEDS THE MAXIMUM CHARACTERS (26)"
        else:
            error = ""

        transaction = Transaction(part, currentDate, transactionDesc, error)
        self.transactionList.append(transaction)

    #Checks for errors, returns true if there is an error
    def checkForError(self, part):
        has_error = False
        if len(str(part.getPartNumber())) > 10 and len(part.getPartDescription()) > 26:
            has_error = True
        elif len(str(part.getPartNumber())) > 10:
            has_error = True
        elif len(part.getPartDescription()) > 26:
            has_error = True
        return has_error


    

'''
The inventory of the program.
Handles both the parts list and transactions list.
The needed modules are imported from the library 
'''
from datetime import datetime
from Library.Transaction import Transaction

class Inventory:

    def __init__(self):
        # Initialize an empty list for parts and transactions
        self.partList = []
        self.transactionList = []

    def addPart(self, part):
        # Add a new part to the part list
        self.partList.append(part)

    def addTransaction(self, condition, part, oldPartNumber):
        # Add a new transaction based on the condition
        currentDate = datetime.now().strftime("%Y-%m-%d")
        error = ""
        transactionDesc = ""

        # Set the transaction description based on the condition
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

        # Check for errors in the part
        if self.checkForError(part):
            # Set the appropriate error message
            if len(str(part.getPartNumber())) > 10 and len(part.getPartDescription()) > 26:
                error = "Part Number and Description EXCEEDS MAXIMUM CHARACTERS (10 and 26 Respectively)."
            elif len(str(part.getPartNumber())) > 10:
                error = "Part Number EXCEEDS THE MAXIMUM CHARACTERS (10)"
            elif len(part.getPartDescription()) > 26:
                error = "Part Description EXCEEDS THE MAXIMUM CHARACTERS (26)"
        else:
            error = ""

        # Create a new transaction and add it to the transaction list
        transaction = Transaction(part, currentDate, transactionDesc, error)
        self.transactionList.append(transaction)

    def checkForError(self, part):
        # Check if the part has any errors
        has_error = False
        if len(str(part.getPartNumber())) > 10 and len(part.getPartDescription()) > 26:
            has_error = True
        elif len(str(part.getPartNumber())) > 10:
            has_error = True
        elif len(part.getPartDescription()) > 26:
            has_error = True
        return has_error

    

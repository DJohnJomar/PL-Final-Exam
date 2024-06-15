'''
The transaction class
'''
class Transaction:
    def __init__(self, part, date, transactionDesc, error):
        # Initialize the transaction with part details, date, description, and error message
        self.partNumber = part.getPartNumber()  # Store the part number from the Part object
        self.date = date  # Store the date of the transaction
        self.transactionDesc = transactionDesc  # Store the description of the transaction
        self.error = error  # Store any error message related to the transaction

    def display(self):
        # Print the transaction details in a formatted way
        print("{:<15}{:<15}{:<30}{:<20}".format(self.partNumber, self.date, self.transactionDesc, self.error))
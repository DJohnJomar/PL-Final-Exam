'''
The transaction class
'''
from Library.Part import Part

class Transaction:

    def __init__(self, part:Part, date, transactionDesc, error):
        self.partNumber = part.getPartNumber()
        self.date = date
        self.transactionDesc = transactionDesc
        self.error = error

    def display(self):
        print("{:<15}{:<15}{:<30}{:<20}".format(self.partNumber, self.date, self.transactionDesc, self.error))
'''
The part class
'''
class Part:

    def __init__(self, partNumber, partDescription, price):
        self.partNumber = partNumber
        self.partDescription = partDescription
        self.price = price
    
    def getPartNumber(self):
        return self.partNumber
    
    def getPartDescription(self):
        return self.partDescription
    
    def display(self):
        print(f"{self.partNumber:<15}{self.price:<15}{self.partDescription:<10}")

    def setPartDescription(self, partDescription):
        self.partDescription = partDescription

    def setPrice(self, price):
        self.price = price
    
    def setPartNumber(self, partNumber):
        self.partNumber = partNumber


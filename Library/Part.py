'''
The part class
'''
class Part:
    def __init__(self, part_number, part_desc, part_price):
        # Initialize the part with a part number, description, and price
        self.part_number = part_number
        self.part_desc = part_desc
        self.part_price = part_price

    def getPartNumber(self):
        # Return the part number
        return self.part_number

    def getPartDescription(self):
        # Return the part description
        return self.part_desc

    def getPrice(self):
        # Return the part price
        return self.part_price

    def setPartNumber(self, part_number):
        # Set a new part number
        self.part_number = part_number

    def setPartDescription(self, part_desc):
        # Set a new part description
        self.part_desc = part_desc

    def setPrice(self, part_price):
        # Set a new part price
        self.part_price = part_price

    def display(self):
        # Print the part details in a formatted way
        print("{:<15}{:<15}{:<30}".format(self.part_number, self.part_price, self.part_desc))
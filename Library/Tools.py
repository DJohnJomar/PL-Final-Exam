'''
Contains the majority of the program's function
Here, the processing of commands and transactions is being done
The needed modules are imported from the library 
'''

from Library.Inventory import Inventory
from Library.Part import Part

class Tools:


    def __init__(self):
        self.inventory = Inventory()


    #Function to run the menu
    def menu(self):
        commandList = ["a", "A", "c", "C", "d", "D", "p", "P", "t", "T", "x", "X"]
        try:
            print("\n\n[A] Add")
            print("[C] Change")
            print("[D] Delete")
            print("[P] View Parts")
            print("[T] View Transactions")
            print("[X] Exit")
            command = input("Enter your choice:")

            #If command exist, handle it
            #If not, reject command
            if command not in commandList:
                print("Command does not exist, please try again. ")
            else:
                self.commandHandler(command)

        except Exception as e:
            print(e)

    #Handles the command
    def commandHandler(self, command):
        #if command is a/A - adding of part
        #Asks for part num, desc, and price
        if command.lower() == 'a':
            alreadyExist = False

            partNumber = input("\nEnter Part Number: ")
            for part in self.inventory.partList:
                if partNumber == part.getPartNumber():
                    alreadyExist = True
            
            if not alreadyExist:
                partDesc = input("Enter part description: ")
                partPrice = input("Enter part price: ")
                part = Part(partNumber, partDesc, partPrice)
                self.inventory.addPart(part)
                self.inventory.addTransaction(1, part, 0)
                print("New part added successfully!")
            else:
                print("Part number already exist, please try a new part number.")

        #If command is c/C
        #Asks which attribute is to be changed in the part (choice 1-3)
        #If attribute is selected, the part is to be found and the changing of attribute is done
        elif command.lower() == 'c':
            if len(self.inventory.partList) == 0:
                print("Command unsucessful, there are no parts yet. ")
                return

            print("\n[1] Description")
            print("[2] Price")
            print("[3] Part Number")
            choice = input("Enter your choice: ")
            if choice not in ['1', '2', '3']:
                print("Command does not exist")
                return

            partNumber = input("\nEnter part Number: ")
            isFound = False
            
            if choice == '1':
                for part in self.inventory.partList:
                    if part.getPartNumber() == partNumber:
                        newDesc = input("\nEnter new description: ")
                        part.setPartDescription(newDesc)
                        self.inventory.addTransaction(2, part, 0)
                        isFound = True
                        print("Part's description is changed successfully!")
                if isFound == False:
                    print("The part was not found.")
            
            if choice == '2':
                for part in self.inventory.partList:
                    if part.getPartNumber() == partNumber:
                        newPrice = input("\nEnter new price: ")
                        part.setPrice(newPrice)
                        self.inventory.addTransaction(3, part, 0)
                        isFound = True
                        print("Part's price changed successfully!")
                if isFound == False:
                    print("The part was not found.")

            if choice == '3':
                for part in self.inventory.partList:
                    if part.getPartNumber() == partNumber:
                        oldPartNumber = part.getPartNumber()
                        newNumber = input("\nEnter new part number: ")
                        part.setPartNumber(newNumber)
                        self.inventory.addTransaction(4, part, oldPartNumber)
                        isFound = True
                        print("Part number is changed successfully!")
                if isFound == False:
                    print("The part was not found.")

        #If command is d/D
        #Deletes the selected part based on part Number
        elif command.lower() == 'd':
            if len(self.inventory.partList) == 0:
                print("Command unsucessful, there are no parts yet. ")
                return
            partNumber = input("\nEnter part number: ")
            isFound = False

            for part in self.inventory.partList:
                if part.getPartNumber() == partNumber:
                    self.inventory.addTransaction(5, part, 0)
                    self.inventory.partList.remove(part)
                    isFound = True
                    print("Part deleted!")
                    break
            
            if isFound == False:
                print("The part was not found.")

        #If the command is p/P, displays the parts
        elif command.lower() == 'p':
            print("\n{:15s}{:15s}{:10s}".format("Part #", "Part Price", "Part Description"))
            for part in self.inventory.partList:
                part.display()
        #If the command is t/T, displays all of the transactions done
        elif command.lower() == 't':
            print("\n{:15s}{:15s}{:30s}{:20s}".format("Part #", "Date", "Transaction Description", "Error"))
            for transaction in self.inventory.transactionList:
                transaction.display()
        #if command is x/X, exits the program
        elif command.lower() == 'x':
            print("Thank you and Good bye")
            exit()  # Exits the program

            

            



         
        

'''
Part-Inventory transactions management in python using libraries.
The main class basically just calls a function of the Tools class located in the Library folder and the Tools module handles the rest.
The main class imports the necessary modules needed - the Tools module from the library
3CS-A || Dimaunahan, Meneses
'''

#Part-Inventory transactions management in python using libraries
#3CS-A || Dimaunahan, Meneses

from Library.Tools import Tools




def main():
    #Creates a tools object
    tools = Tools()
    print("Welcome to the Parts-Inventory Management, now in Python using libraries!")
    while True:
        try:
            #Calls the menu function of tools
            tools.menu()
        except Exception:
            print("An error occured, please try again")

if __name__ == "__main__":
    main()

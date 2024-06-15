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
    # Create an instance of the Tools class, which initializes the inventory management system
    tools = Tools()
    # Run the main loop of the Tkinter GUI application
    tools.run()

if __name__ == "__main__":
    # Call the main function to start the application
    main() 
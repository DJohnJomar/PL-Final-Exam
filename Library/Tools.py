'''
Contains the majority of the program's function
Here, the processing of commands and transactions is being done
The needed modules are imported from the library 
'''

from Library.Inventory import Inventory
from Library.Part import Part
from tkinter import *
from tkinter import messagebox

class Tools:

    def __init__(self):
        self.inventory = Inventory()
        self.initUI()

    def initUI(self):
       # Initialize the main window
        self.root = Tk()
        self.root.title("Parts Inventory Management")
        self.root.geometry("500x400")  # Set the width to 500 pixels and height to 400 pixels

       # Create header text at the top
        title_label = Label(self.root, text="Parts Inventory Management", font=('Helvetica', 18, 'bold'))
        title_label.pack(pady=10)

        # Create the menu frame
        menu_frame = Frame(self.root)
        menu_frame.pack(pady=20, padx=20)

        # Define button font
        button_font = ('Helvetica', 12)

        # Add buttons to the menu frame, vertically aligned and centered
        Button(menu_frame, text="Add Part", command=self.add_part_ui, font=button_font, height=2, width=20).pack(fill=X, pady=5)
        Button(menu_frame, text="Change Part", command=self.change_part_ui, font=button_font, height=2, width=20).pack(fill=X, pady=5)
        Button(menu_frame, text="Delete Part", command=self.delete_part_ui, font=button_font, height=2, width=20).pack(fill=X, pady=5)
        Button(menu_frame, text="View Parts", command=self.view_parts_ui, font=button_font, height=2, width=20).pack(fill=X, pady=5)
        Button(menu_frame, text="View Transactions", command=self.view_transactions_ui, font=button_font, height=2, width=20).pack(fill=X, pady=5)
        Button(menu_frame, text="Exit", command=self.root.quit, font=button_font, height=2, width=20).pack(fill=X, pady=5)
    def run(self):
        # Run the main loop
        self.root.mainloop()

    def add_part_ui(self):
        # Function to add a new part
        def add_part():
            part_number = part_number_entry.get()
            part_desc = part_desc_entry.get()
            part_price = part_price_entry.get()

            # Check if the part already exists
            already_exist = False
            for part in self.inventory.partList:
                if part_number == part.getPartNumber():
                    already_exist = True

            if not already_exist:
                # Add the new part to the inventory
                part = Part(part_number, part_desc, part_price)
                self.inventory.addPart(part)
                self.inventory.addTransaction(1, part, 0)
                messagebox.showinfo("Success", "New part added successfully!")
                add_part_window.destroy()  # Close the window
            else:
                messagebox.showerror("Error", "Part number already exists, please try a new part number.")

        # Create the add part window
        add_part_window = Toplevel(self.root)
        add_part_window.title("Add Part")

        # Add input fields and labels
        Label(add_part_window, text="Part Number").grid(row=0, column=0, padx=10, pady=10)
        part_number_entry = Entry(add_part_window)
        part_number_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(add_part_window, text="Part Description").grid(row=1, column=0, padx=10, pady=10)
        part_desc_entry = Entry(add_part_window)
        part_desc_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(add_part_window, text="Part Price").grid(row=2, column=0, padx=10, pady=10)
        part_price_entry = Entry(add_part_window)
        part_price_entry.grid(row=2, column=1, padx=10, pady=10)

        Button(add_part_window, text="Add Part", command=add_part).grid(row=3, column=0, columnspan=2, pady=10)

    def change_part_ui(self):
        # Function to change an existing part
        def change_part():
            part_number = part_number_entry.get()
            attribute = attribute_var.get()
            new_value = new_value_entry.get()

            # Find the part in the inventory
            part = None
            for p in self.inventory.partList:
                if p.getPartNumber() == part_number:
                    part = p
                    break

            if part:
                # Change the selected attribute of the part
                if attribute == "Description":
                    part.setPartDescription(new_value)
                    self.inventory.addTransaction(2, part, 0)
                    messagebox.showinfo("Success", "Part's description changed successfully!")
                    change_part_window.destroy()  # Close the window
                elif attribute == "Price":
                    part.setPrice(new_value)
                    self.inventory.addTransaction(3, part, 0)
                    messagebox.showinfo("Success", "Part's price changed successfully!")
                    change_part_window.destroy()  # Close the window
                elif attribute == "Part Number":
                    old_part_number = part.getPartNumber()
                    part.setPartNumber(new_value)
                    self.inventory.addTransaction(4, part, old_part_number)
                    messagebox.showinfo("Success", "Part number changed successfully!")
                    change_part_window.destroy()  # Close the window
            else:
                messagebox.showerror("Error", "The part was not found.")

        # Create the change part window
        change_part_window = Toplevel(self.root)
        change_part_window.title("Change Part")

        # Add input fields and labels
        Label(change_part_window, text="Part Number").grid(row=0, column=0, padx=10, pady=10)
        part_number_entry = Entry(change_part_window)
        part_number_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(change_part_window, text="Attribute to Change").grid(row=1, column=0, padx=10, pady=10)
        attribute_var = StringVar(value="Description")
        OptionMenu(change_part_window, attribute_var, "Description", "Price", "Part Number").grid(row=1, column=1, padx=10, pady=10)

        Label(change_part_window, text="New Value").grid(row=2, column=0, padx=10, pady=10)
        new_value_entry = Entry(change_part_window)
        new_value_entry.grid(row=2, column=1, padx=10, pady=10)

        Button(change_part_window, text="Change Part", command=change_part).grid(row=3, column=0, columnspan=2, pady=10)

    def delete_part_ui(self):
        # Function to delete an existing part
        def delete_part():
            part_number = part_number_entry.get()

            # Find the part in the inventory
            part = None
            for p in self.inventory.partList:
                if p.getPartNumber() == part_number:
                    part = p
                    break

            if part:
                # Delete the part from the inventory
                self.inventory.addTransaction(5, part, 0)
                self.inventory.partList.remove(part)
                messagebox.showinfo("Success", "Part deleted successfully!")
                delete_part_window.destroy()  # Close the window
            else:
                messagebox.showerror("Error", "The part was not found.")

        # Create the delete part window
        delete_part_window = Toplevel(self.root)
        delete_part_window.title("Delete Part")

        # Add input field and label
        Label(delete_part_window, text="Part Number").grid(row=0, column=0, padx=10, pady=10)
        part_number_entry = Entry(delete_part_window)
        part_number_entry.grid(row=0, column=1, padx=10, pady=10)

        Button(delete_part_window, text="Delete Part", command=delete_part).grid(row=1, column=0, columnspan=2, pady=10)

    def view_parts_ui(self):
        # Function to view all parts
        view_parts_window = Toplevel(self.root)
        view_parts_window.title("View Parts")

        # Create a text widget to display parts
        parts_text = Text(view_parts_window, width=50, height=20)
        parts_text.pack(pady=10)

        # Add headers
        parts_text.insert(END, "{:<15}{:<15}{:<30}\n".format("Part #", "Part Price", "Part Description"))
        # Add part details
        for part in self.inventory.partList:
            parts_text.insert(END, "{:<15}{:<15}{:<30}\n".format(part.getPartNumber(), part.getPrice(), part.getPartDescription()))

        parts_text.config(state=DISABLED)

    def view_transactions_ui(self):
        # Function to view all transactions
        view_transactions_window = Toplevel(self.root)
        view_transactions_window.title("View Transactions")

        # Create a text widget to display transactions
        transactions_text = Text(view_transactions_window, width=70, height=20)  # Increase the width to 70
        transactions_text.pack(pady=10)

        # Add headers
        transactions_text.insert(END, "{:<15}{:<15}{:<30}{:<20}\n".format("Part #", "Date", "Transaction Description", "Error"))
        # Add transaction details
        for transaction in self.inventory.transactionList:
            transactions_text.insert(END, "{:<15}{:<15}{:<30}{:<20}\n".format(transaction.partNumber, transaction.date, transaction.transactionDesc, transaction.error))

        transactions_text.config(state=DISABLED)

            

            



         
        

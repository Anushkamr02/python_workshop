import csv
import os
class Inventory:
    def __init__(self):
        self.items = {}

    def create_item(self, name, price):
        self.items[name] = price
        print(f"Item '{name}' added successfully.")

    def update_item(self, name, price):
        if name in self.items:
            self.items[name] = price
            print(f"Item '{name}' updated successfully.")
        else:
            print("Item not found.")

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Item '{name}' deleted successfully.")
        else:
            print("Item not found.")

    def read_items(self):
        if self.items:
            for name, price in self.items.items():
                print(f"{name}: ${price}")
        else:
            print("No items available.")

inventory = Inventory()

def owner():
    while True:
        print("\nOwner Menu:\n1. Create item\n2. Update item\n3. Delete item\n4. Read items\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            inventory.create_item(name, price)
        elif choice == "2":
            name = input("Enter item name: ")
            price = float(input("Enter new price: "))
            inventory.update_item(name, price)
        elif choice == "3":
            name = input("Enter item name to delete: ")
            inventory.delete_item(name)
        elif choice == "4":
            inventory.read_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def dealer():
    while True:
        print("\nDealer Menu:\n1. Provide item to owner\n2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter item name to provide: ")
            price = float(input("Enter price of the item: "))
            inventory.create_item(name, price)
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

def customer():
    while True:
        print("\nCustomer Menu:\n1. View items\n2. Buy item\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            inventory.read_items()
        elif choice == "2":
            name = input("Enter item name to buy: ")
            if name in inventory.items:
                print(f"Item '{name}' purchased successfully for ${inventory.items[name]}.")
            else:
                print("Item not available.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
while True:
    role = input("\nEnter your role (owner, dealer, customer) or type 'exit' to quit: ").lower()

    if role == "owner":
        owner()
    elif role == "dealer":
        dealer()
    elif role == "customer":
        customer()
    elif role == "exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid role. Please enter again.")

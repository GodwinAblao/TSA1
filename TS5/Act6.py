class Item:
    def __init__(self, item_id, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        try:
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        try:
            if price is not None and price < 0:
                raise ValueError("Price cannot be negative.")
            if name:
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description
            if price is not None:
                self.items[item_id].price = price
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item not found.")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("[C] Create Item")
        print("[R] Read Items")
        print("[U] Update Item")
        print("[D] Delete Item")
        print("[Q] Quit")

        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        if choice == 'C':
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price input. Please enter a valid number.")

        elif choice == 'R':
            manager.read_items()

        elif choice == 'U':
            item_id = input("Enter item ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            description = input("Enter new description (leave blank to keep current): ") or None
            try:
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price input. Please enter a valid number.")
        
        elif choice == 'D':
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
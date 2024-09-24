class Product:
    def __init__(self, name, quantity, restock_time):
        self.name = name
        self.quantity = quantity
        self.restock_time = restock_time
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, product):
        if self.root is None:
            self.root = product
        else:
            self._insert_recursive(self.root, product)
    
    def _insert_recursive(self, current, product):
        if product.name < current.name:
            if current.left is None:
                current.left = product
            else:
                self._insert_recursive(current.left, product)
        else:
            if current.right is None:
                current.right = product
            else:
                self._insert_recursive(current.right, product)
    
    def search(self, name):
        return self._search_recursive(self.root, name)
    
    def _search_recursive(self, current, name):
        if current is None:
            return None
        if name == current.name:
            return current
        elif name < current.name:
            return self._search_recursive(current.left, name)
        else:
            return self._search_recursive(current.right, name)
    
    def display_stock(self):
        self._display_stock_recursive(self.root)
    
    def _display_stock_recursive(self, current):
        if current is not None:
            self._display_stock_recursive(current.left)
            print(f'Product: {current.name}, Quantity: {current.quantity}, Restock Time: {current.restock_time}')
            self._display_stock_recursive(current.right)

class InventoryManagementSystem:
    def __init__(self):
        self.stock = BinaryTree()
    
    def add_product(self, name, quantity, restock_time):
        product = Product(name, quantity, restock_time)
        self.stock.insert(product)
    
    def check_stock(self, name):
        product = self.stock.search(name)
        if product:
            if product.quantity <= product.restock_time:
                print(f'Product {product.name} is below critical level. Automatically placing restock order.')
                self.place_restock_order(product)
            else:
                print(f'Product {product.name} is available.')
        else:
            print(f'Product {name} not found in stock.')
    
    def process_order(self, name, quantity):
        product = self.stock.search(name)
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f'Order of {quantity} units of {product.name} processed.')
                self.check_stock(name)
            else:
                print(f'Product {product.name} does not have enough quantity for the order.')
        else:
            print(f'Product {name} not found in stock.')
    
    def buy_product(self, name, quantity):
        product = self.stock.search(name)
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f'Bought {quantity} units of {product.name}.')
                self.check_stock(name)
            else:
                print(f'Not enough {product.name} in stock to complete the purchase.')
        else:
            print(f'Product {name} not found in stock.')

    def place_restock_order(self, product):
        restock_amount = 10
        product.quantity += restock_amount
        print(f'Restock order placed for {restock_amount} units of {product.name}. New quantity: {product.quantity}.')

def main():
    system = InventoryManagementSystem()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Check Stock")
        print("3. Process Order")
        print("4. Buy Product")
        print("5. Display Stock")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            restock_time = int(input("Enter restock time: "))
            system.add_product(name, quantity, restock_time)
            print(f'Product {name} added.')
        
        elif choice == '2':
            name = input("Enter product name to check stock: ")
            system.check_stock(name)
        
        elif choice == '3':
            name = input("Enter product name to process order: ")
            quantity = int(input("Enter quantity to order: "))
            system.process_order(name, quantity)
        
        elif choice == '4':
            name = input("Enter product name to buy: ")
            quantity = int(input("Enter quantity to buy: "))
            system.buy_product(name, quantity)
        
        elif choice == '5':
            print("Current Stock:")
            system.stock.display_stock()
        
        elif choice == '6':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

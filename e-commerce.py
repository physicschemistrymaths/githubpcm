#ecommerce

import uuid
from datetime import datetime

class product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (category: {self.category})"
    


class category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, products):
        self.products.append(products)

    def list_product(self):
        return self.products
    


class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.orders = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        return self.cart
    
    def checkout(self):
        total = sum(product.price for product in self.cart)
        order = order(self.username, self.cart, total)
        self.order.append(order)
        self.cart.clear()
        return order
    


    class order:
        def __init__(self, username, products, total_amount):
            self.username = username
            self.products = products
            self.total_amount = total_amount
            self.date = datetime.now()
        
        def __str__(self):
            product_list = ',' .join([product.name for product in self.products])
            return f"Order ID: {self.id}\nProducts: {product_list}\nTotal: ${self.total_amount:.2f}\nDate: {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
        


class inventory:
    def __init__(self):
        self.products = {}
        self.categories = {}

    def add_product(self, product):
        if product.category not in self.categories:
            self.categories[product.category] = category(product.category)
        self.categories[product.category].add_product(product)
        self.products[product.id] = product

    def get_product(self, product_id):
        return self.products.get(product_id)
    
    def list_products(self):
        return self.products.values()
    
    def list_categories(self):
        return self.categories.values()
    


class ecommercesystem:
    def __init__(self):
        self.inventory = inventory()
        self.user = {}
        self.current_user = None

    def register_user(self, username, password):
        if username in self.register_user:
            print("User Already Exist")
        else:
            self.user[username] = user(username, password)
            print("User Register Successfully")

    def login_user(self, username, password):
        user = self.user.get(username)
        if user and user.password == password:
            self.current_user = user
            print("Login Successfully.")
        else:
            print("Invalid username or Password")

    def list_products(self):
        for products in self.inventory.list_products():
            print(products)

    def add_to_cart(self, product_id):
        if self.current_user:
            product = self.inventory.get_product(product_id)
            if product:
                self.current_user.add_to_cart(product)
                print(f"Added {product.name} to cart.")
            else:
                print("Product Not Found")
        else:
            print("Please Login First.")

    def view_cart(self):
        if self.current_user:
            for product in self.current_user.view_cart():
                print(product)
        else:
            print("Please login first.")

    def checkout(self):
        if self.current_user:
            order = self.current_user.checkout()
            print("Checkout Completed")
            print(order)
        else:
            print("Please login first.")

    def view_order_history(self):
        if self.current_user:
            for order in self.current_user.orders:
                print(order)
        else:
            print("Please login first.")

    def main():
        system = ecommercesystem()


        system.inventory.add_product(product(1, "Laptop", 999.99, "Electronics"))
        system.inventory.add_product(product(2,"Headphones", 199.99, "Electronics"))
        system.inventory.add_product(product(3, "Keyboard", 49.99, "Electronics"))
        system.inventory.add_product(product(4, "Coffe Maker", 89.99, "Home Appliances"))

        while True:
            print("\n--- E-Commerce Store ---")
            if system.current_user:
                print(f"Loged in as: {system.current_user.username}")
            print("1. Register")
            print("2. Login")
            print("3. List Products")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Checkout")
            print("7. View Order History")
            print("8. Exit")

            choice = input("Choose an option:")

            if choice == '1':
                username = input("Enter Username:")
                password = input("Enter Password:")
                system.register_user(username, password)

            elif choice == '2':
                username = input("Enter Username:")
                password = input("Enter Password:")
                system.register_user(username, password)

            elif choice == '3':
                system.list_products()

            elif choice == '4':
                product_id = int(input("Enter Product ID to add to cart:"))
                system.add_to_cart(product_id)

            elif choice == '5':
                system.view_cart()
            
            elif choice == '6':
                system.checkout()

            elif choice == '7':
                system.view_order_history()

            elif choice == '8':
                print ("Exiting Ecommerce Store")
                break
            
            else:
                print("Invalid Choice. Please try again")
                                                                                                    
    if __name__ == '__main__':
        main()


        


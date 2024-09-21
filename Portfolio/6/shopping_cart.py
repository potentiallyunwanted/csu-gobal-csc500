
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"
    
    def set_item(self):
        self.item_name = input("Enter the item name: ") or self.item_name
        self.item_description = input("Enter the item description: ") or self.item_description
        self.item_price = float(input("Enter the item price: ") or self.item_price)
        self.item_quantity = int(input("Enter the item quantity: ") or self.item_quantity)

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self):
        self.cart_items = []
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        
    def add_item(self):
        item = ItemToPurchase()
        item.set_item()
        self.cart_items.append(item)
        print(f"{item.item_name} successfully added.\n")
        
    def remove_item(self):
        item_name = input("Enter name of item to remove: ")
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f"{item_name} removed.")
                return
        print(f"{item_name} not found. Nothing removed.")
        
    def modify_item(self, itemToPurchase):
        for item in self.cart_items:
            if item.item_name == itemToPurchase:
                print(f"{itemToPurchase} found.")
                if item.item_quantity == 0 and item.item_name == "none" and item.item_price == 0.0 and item.item_description == "none":
                    print(f"{itemToPurchase} found, but does not have any information.")
                    print("Please add the item to the cart first.")
                else:
                    new_name = input("Enter the new name: ")
                    item.item_name = new_name
                    print(f"{itemToPurchase} name updated.")
                    new_quantity = int(input("Enter the new quantity: "))
                    item.item_quantity = new_quantity
                    print(f"{itemToPurchase} quantity updated.")
                    new_price = float(input("Enter the new price: "))
                    item.item_price = new_price
                    print(f"{itemToPurchase} price updated.")
                    new_description = input("Enter the new description: ")
                    item.item_description = new_description
                    print(f"{itemToPurchase} description updated.")
                print(f"{itemToPurchase} successfully modified.")
                return True
        print(f"{itemToPurchase} not found. Nothing modified.")
    
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            item_cost = item.item_price * item.item_quantity
            total_cost += item_cost
        return total_cost
        
    def print_total(self):
        number_of_items = self.get_num_items_in_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"No. of Items: {number_of_items}\n")
        print("===================================")
        print("TOTAL COST\n")
        for item in self.cart_items:
            item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY\n")
        else:
            print(f"Total: ${total_cost:.2f}\n")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions\n")
        print("===================================")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}\n")

def print_menu(shopping_cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "m - Modify item\n"
        "d - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    print(menu)
    menu_choice = input("Choose an option: ")
    while True:
        while menu_choice not in ['a', 'r', 'm', 'd', 'o', 'q']:
            menu_choice = input("Choose an option: ")
        if menu_choice == 'q':
            print("Have a great day! Goodbye.")
            return False
        elif menu_choice == 'a':
            shopping_cart.add_item()
            menu_choice = input("Choose an option: ")
        elif menu_choice == 'r':
            shopping_cart.remove_item()
            menu_choice = input("Choose an option: ")
        elif menu_choice == 'm':
            item_to_modify = input("Enter the item to modify: ")
            shopping_cart.modify_item(item_to_modify)
            menu_choice = input("Choose an option: ")
        elif menu_choice == 'd':
            shopping_cart.print_descriptions()
            menu_choice = input("Choose an option: ")
        elif menu_choice == 'o':
            shopping_cart.print_total()
            menu_choice = input("Choose an option: ")



def main():
    shopping_cart = ShoppingCart()
    print_menu(shopping_cart)
    

if __name__ == "__main__":
    main()
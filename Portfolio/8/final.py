import difflib

# pseudocode
# Add_item
# Create new Item instance
# Set item_name using validate_input with expected_type 'string' and non-empty condition
# Set item_description using validate_input with expected_type 'string' and non-empty condition
# Set item_price using validate_input with expected_type 'float' and condition value >= 0
# Set item_quantity using validate_input with expected_type 'int' and condition value >= 0
# Add Item instance to cart's item list
# Display message confirming item was added

# Remove_item
# Get item_name to remove using validate_input with expected_type 'string' and non-empty condition
# For each item in cart's item list:
# If item's name matches item_name:
# Remove item from cart's item list
# Display message confirming item was removed
# Return
# Display message indicating item was not found and nothing was removed

# Modify_item
# Get item_name to modify using validate_input with expected_type 'string' and non-empty condition
# For each item in cart's item list:
# If item's name matches item_name:
# Display message confirming item was found
# Set new_name using validate_input with expected_type 'string' and non-empty condition
# Update item's name to new_name
# Set new_quantity using validate_input with expected_type 'int' and condition value >= 0
# Update item's quantity to new_quantity
# Set new_price using validate_input with expected_type 'float' and condition value >= 0
# Update item's price to new_price
# Set new_description using validate_input with expected_type 'string' and non-empty condition
# Update item's description to new_description
# Display message confirming item was modified
# Return
# Display message indicating item was not found and nothing was modified

# validate_input
# Prompt the user for input and store the response in user_input
# If a condition function is provided, apply it to user_input
# If the condition returns True, return the valid user_input
# If the condition returns False, display the error message or a default message
# If no condition is provided, check if user_input is not empty after stripping whitespace
# If input is valid, return user_input
# If input is empty, display the error message or a default message

def validate_input(prompt, expected_type, condition=None, error_message=None):
    while True:
        user_input = input(prompt)
        if expected_type == 'string':
            if condition:
                if condition(user_input):
                    return user_input
                else:
                    print(error_message or "Invalid input.")
            else:
                if user_input.strip() != '':
                    return user_input
                else:
                    print(error_message or "Input cannot be empty.")
        elif expected_type == 'int':
            try:
                value = int(user_input)
                if condition:
                    if condition(value):
                        return value
                    else:
                        print(error_message or "Invalid number.")
                else:
                    return value
            except ValueError:
                print(error_message or "Please enter a valid integer.")
        elif expected_type == 'float':
            try:
                value = float(user_input)
                if condition:
                    if condition(value):
                        return value
                    else:
                        print(error_message or "Invalid number.")
                else:
                    return value
            except ValueError:
                print(error_message or "Please enter a valid number.")
        else:
            raise ValueError("Unsupported expected_type.")

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"
        
    def set_item(self):
        self.item_name = validate_input(
            "Enter the item name: ",
            'string',
            condition=lambda s: s.strip() != '',
            error_message="Item name cannot be empty."
        )

        self.item_description = validate_input(
            "Enter the item description: ",
            'string',
            condition=lambda s: s.strip() != '',
            error_message="Item description cannot be empty."
        )

        self.item_price = validate_input(
            "Enter the item price: ",
            'float',
            condition=lambda v: v >= 0,
            error_message="Price must be a non-negative number."
        )

        self.item_quantity = validate_input(
            "Enter the item quantity: ",
            'int',
            condition=lambda v: v >= 0,
            error_message="Quantity must be a non-negative integer."
        )
    
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
        item_name = validate_input(
            "Enter name of item to remove: ",
            'string',
            condition=lambda s: s.strip() != '',
            error_message="Item name cannot be empty."
        )
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

                new_name = validate_input(
                    "Enter the new name: ",
                    'string',
                    condition=lambda s: s.strip() != '',
                    error_message="Item name cannot be empty."
                )
                item.item_name = new_name
                print(f"{itemToPurchase} name updated.")

                new_quantity = validate_input(
                    "Enter the new quantity: ",
                    'int',
                    condition=lambda v: v >= 0,
                    error_message="Quantity must be a non-negative integer."
                )
                item.item_quantity = new_quantity
                print(f"{itemToPurchase} quantity updated.")

                new_price = validate_input(
                    "Enter the new price: ",
                    'float',
                    condition=lambda v: v >= 0,
                    error_message="Price must be a non-negative number."
                )
                item.item_price = new_price
                print(f"{itemToPurchase} price updated.")

                new_description = validate_input(
                    "Enter the new description: ",
                    'string',
                    condition=lambda s: s.strip() != '',
                    error_message="Item description cannot be empty."
                )
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
    menu_choice = input("Choose an option: ").strip().lower()
    while True:
        while menu_choice not in ['a', 'r', 'm', 'd', 'o', 'q']:
            menu_choice = input("Choose an option: ").strip().lower()
        if menu_choice == 'q':
            print("Have a great day! Goodbye.")
            return False
        elif menu_choice == 'a':
            shopping_cart.add_item()
            print(menu)
            menu_choice = input("Choose an option: ").strip().lower()
        elif menu_choice == 'r':
            shopping_cart.remove_item()
            print(menu)
            menu_choice = input("Choose an option: ").strip().lower()
        elif menu_choice == 'm':
            item_to_modify = validate_input(
                "Enter the item to modify: ",
                'string',
                condition=lambda s: s.strip() != '',
                error_message="Item name cannot be empty."
            )
            shopping_cart.modify_item(item_to_modify)
            print(menu)
            menu_choice = input("Choose an option: ").strip().lower()
        elif menu_choice == 'd':
            shopping_cart.print_descriptions()
            print(menu)
            menu_choice = input("Choose an option: ").strip().lower()
        elif menu_choice == 'o':
            shopping_cart.print_total()
            print(menu)
            menu_choice = input("Choose an option: ").strip().lower()


def banner():
    RED = "\33[91m"
    print(f"""" {RED}
          ____ ____   ____ ____   ___   ___        _ 
         / ___/ ___| / ___| ___| / _ \ / _ \      / |
        | |   \___ \| |   |___ \| | | | | | |_____| |
        | |___ ___) | |___ ___) | |_| | |_| |_____| |
         \____|____/ \____|____/ \___/ \___/      |_|
         / ___|| |__   ___  _ __  _ __ (_)_ __   __ _ 
         \___ \| '_ \ / _ \| '_ \| '_ \| | '_ \ / _` |
          ___) | | | | (_) | |_) | |_) | | | | | (_| |
         |____/|_| |_|\___/| .__/| .__/|_|_| |_|\__, |
           ____    _    ___|_|___|_|  ____ _    |___/ 
          / ___|  / \  |  _ \_   _|  / ___| |   |_ _| 
         | |     / _ \ | |_) || |   | |   | |    | |  
         | |___ / ___ \|  _ < | |   | |___| |___ | |  
          \____/_/   \_\_| \_\|_|    \____|_____|___| 
          """)

def validate_month(prompt, valid_months):
    while True:
        user_input = input(prompt).strip()
        # Standardize the input to capitalize the first letter
        user_input_cap = user_input.capitalize()
        if user_input_cap in valid_months:
            return user_input_cap
        else:
            # Use difflib to find close matches
            matches = difflib.get_close_matches(user_input_cap, valid_months, n=1, cutoff=0.6)
            if matches:
                suggestion = matches[0]
                print(f"Did you mean '{suggestion}'?")
                # Prompt the user to confirm the suggestion
                confirm = input("Enter 'y' for yes or 'n' for no: ").strip().lower()
                if confirm == 'y':
                    return suggestion
                else:
                    print("Please try again.")
            else:
                print("Invalid month name. Please try again.")

def main():
    banner()
    shopping_cart = ShoppingCart()

    valid_months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    first_name = validate_input(
        "Enter your first name: ",
        expected_type='string',
        condition=lambda s: s.strip() != '',
        error_message="First name cannot be empty."
    )
    
    last_name = validate_input(
        "Enter your last name: ",
        expected_type='string',
        condition=lambda s: s.strip() != '',
        error_message="Last name cannot be empty."
    )
    
    month = validate_month(
        "Enter today's Month: ",
        valid_months
    )
    # Standardize the month to capitalize the first letter
    month = month.strip().capitalize()
    
    day = validate_input(
        "Enter today's day as a number: ",
        expected_type='int',
        condition=lambda v: 1 <= v <= 31,
        error_message="Day must be a number between 1 and 31."
    )
    
    year = validate_input(
        "Enter today's year: ",
        expected_type='int',
        condition=lambda v: v >= 0,
        error_message="Year must be a positive integer."
    )
    
    shopping_cart.customer_name = f"{first_name} {last_name}"
    shopping_cart.current_date = f"{month} {day}, {year}"
    print_menu(shopping_cart)

    

if __name__ == "__main__":
    main()
'''
Step 1: Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()
Example of print_item_cost() output:
Bottled Water 10 @ $1 = $10


Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Example:

Item 1

Enter the item name:

Chocolate Chips

Enter the item price:

3

Enter the item quantity:

1

Item 2

Enter the item name:

Bottled Water

Enter the item price:

1

Enter the item quantity:

10


Step 3: Add the costs of the two items together and output the total cost.

Example:

TOTAL COST

Chocolate Chips 1 @ $3 = $3

Bottled Water 10 @ $1 = $10

Total: $13

Your program submission materials must include your source code and screenshots of the application executing the code and the results. Please refer to the video as a recourse and reference: Python Classes and Objects (With Examples)Links to an external site..
'''
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    def set_item(self):
        self.item_name = input("Enter the item name: ") or self.item_name
        self.item_price = float(input("Enter the item price: ") or self.item_price)
        self.item_quantity = int(input("Enter the item quantity: ") or self.item_quantity)

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self):
        self.items = [] 
        
    def add_item(self):
        item = ItemToPurchase()
        item.set_item()
        self.items.append(item)
        print(f"{item.item_name} successfully added.\n")

    def print_total_cost(self):
        total_cost = 0
        print("\nTOTAL COST")
        for item in self.items:
            item_cost = item.item_price * item.item_quantity
            total_cost += item_cost
            item.print_item_cost()
        print(f"\nTotal: ${total_cost:.2f}")


def main():
    shopping_cart = ShoppingCart()
    
    add_more_items = True
    while add_more_items:
        shopping_cart.add_item()
        add_more = input("Would you like to add another item? (y/n): ").lower()
        if add_more == 'n':
            if len(shopping_cart.items) < 2:
                print("Please add at least two items.")
            else:
                add_more_items = False
    
    shopping_cart.print_total_cost()

if __name__ == "__main__":
    main()

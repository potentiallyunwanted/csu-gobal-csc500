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
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}")
    
def main():
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: ").strip('$').strip())
    item1.item_quantity = int(input("Enter the item quantity: "))
    
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: ").strip('$').strip())
    item2.item_quantity = int(input("Enter the item quantity: "))
    
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
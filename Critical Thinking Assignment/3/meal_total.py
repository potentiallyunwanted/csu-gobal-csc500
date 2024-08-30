#Instructions
# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food
# calculate the amounts with an 
# 18 percent tip and
# 7 percent sales tax. 
# Display each of these amounts and the total price.

'''
Sudo code:
1. Create a class called Meal
2. Create a constructor that takes in the food_charge
3. Create a tip and tax variable and assign them 0.18 and 0.07 respectively
4. Create a tip_amount variable and assign it to food_charge * tip
5. Create a tax_amount variable and assign it to food_charge * tax
6. Create a total variable and assign it to food_charge + tip_amount + tax_amount
7. Create a display method that prints the food_charge, tip_amount, tax_amount, and total
8. Create a main function that takes in the food_charge from the user
9. Create an instance of the Meal class with the food_charge
10. Call the display method on the instance of the Meal class
'''

class Meal:
    def __init__(self,food_charge):
        self.food_charge = food_charge
        self.tip = 0.18
        self.tax = 0.07
        self.tip_amount = self.food_charge * self.tip
        self.tax_amount = self.food_charge * self.tax
        self.total = self.food_charge + self.tip_amount + self.tax_amount

    def display(self):
        print(f"Food Charge: ${self.food_charge:.2f}")
        print(f"Tip: ${self.tip_amount:.2f}")
        print(f"Tax: ${self.tax_amount:.2f}")
        print(f"Total: ${self.total:.2f}")
        
def main():
    food_charge = float(input("Enter the charge for the food: ").strip('$').strip())
    meal = Meal(food_charge)
    meal.display()
    
if __name__ == "__main__":
    main()
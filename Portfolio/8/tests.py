import sys
from unittest.mock import patch
from final import main

# pseudocode code
# Create empty ShoppingCart instance
# Simulate adding items:
# Mock inputs for add_item_to_cart function
# Call add_item_to_cart with mocked inputs
# Verify item was added to cart's item list
# Simulate removing items:
# Mock inputs for remove_item_from_cart function
# Call remove_item_from_cart with mocked inputs
# Verify item was removed from cart's item list
# Simulate modifying items:
# Mock inputs for modify_item_in_cart function
# Call modify_item_in_cart with mocked inputs
# Verify item attributes were updated in cart's item list
# Simulate viewing cart:
# Call function to display cart's items and total cost
# Verify output matches expected results
# Simulate invalid inputs:
# Provide invalid data to input validation functions
# Ensure appropriate error messages are displayed
# Verify that invalid inputs are not accepted

def run_program_with_inputs(inputs):
    input_generator = (input_str for input_str in inputs)

    def mock_input(prompt=''):
        print(prompt, end='')
        try:
            response = next(input_generator)
            print(response)    
            return response
        except StopIteration:
            sys.exit(0)

    with patch('builtins.input', mock_input):
        main()

if __name__ == '__main__':
    simulated_inputs = [
        'John',             
        'Doe',              
        'October',          
        '5',                
        '2024',             
        'a',                
        'Apple',           
        'Fresh red apples', 
        '0.99',            
        '5',                
        'a',                
        'Banana',           
        'Yellow bananas',   
        '0.50',             
        '10',               
        'o',                
        'm',                
        'Apple',            
        'Green Apple',      
        '8',                
        '1.10',             
        'Fresh green apples', 
        'o',                
        'r',                
        'Banana',           
        'd',                
        'q'                 
    ]

    run_program_with_inputs(simulated_inputs)

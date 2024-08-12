class cta1:
    def get_numbers(self):
        self.number1 = input('Number 1: ')
        self.number2 = input('Number 2: ')
    def add(self):
        return f"adding {self.number1} to {self.number2} is {int(self.number1) + int(self.number2)}"
    def subtract(self):
        return f"subtracting {self.number1} from {self.number2} is {int(self.number1) - int(self.number2)}"
    def multiply(self):
        return f"multiplying {self.number1} by {self.number2} is {int(self.number1) * int(self.number2)}"
    def divide(self):
        return f"dividing {self.number1} by {self.number2} is {int(self.number1) / int(self.number2)}"
    def print_results(self, action:str, ):
        action_table = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }
        print(f"{action}:", action_table[action]())
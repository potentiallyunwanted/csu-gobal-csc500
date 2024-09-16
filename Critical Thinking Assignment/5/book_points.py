#Points Calculation Class
#Ask for the number of books bough
#if books <= 1, points = 0
#if books >= 2 and books <= 3, points = 5
#if books >= 4 and books <= 5, points = 15
#if books >= 6 and books <= 7, points = 30
#if books >= 8, points = 60

class BookPoints:
    def __init__(self):
        self.books = 0
        self.points = 0

    def get_points(self):
        self.books = int(input('Enter the number of books bought: '))
        if self.books <= 1:
            self.points = 0
        elif self.books >= 2 and self.books <= 3:
            self.points = 5
        elif self.books >= 4 and self.books <= 5:
            self.points = 15
        elif self.books >= 6 and self.books <= 7:
            self.points = 30
        elif self.books >= 8:
            self.points = 60

    def print_points(self):
        print(f'The number of books bought is {self.books}')
        print(f'The number of points earned is {self.points}')
        
def run_points():
    points = BookPoints()
    points.get_points()
    points.print_points()
    
if __name__ == '__main__':
    run_points()

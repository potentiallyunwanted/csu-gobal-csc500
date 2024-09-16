#pseudo code
#class RainfallCollector
#Attributes
#start_year (int)
#end_year (int)
#total_rainfall (float)
#total_months (int)
#average_rainfall (float)
#rainfall (list)
#months (list)
#Ask for Start year and End year
#Month iterator January to December for each year
#Ask for rainfall in inches for each month
#Calculate the number of months, total rainfall, average rainfall per month for entire period

class RainfallCollector:
    def __init__(self):
        self.start_year = 0
        self.end_year = 0
        self.total_rainfall = 0
        self.total_months = 0
        self.average_rainfall = 0
        self.rainfall = []
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    def get_rainfall(self):
        self.start_year = int(input('Enter the start year: '))
        self.end_year = int(input('Enter the end year: '))
        for year in range(self.start_year, self.end_year + 1):
            for month in self.months:
                try:
                    rainfall = float(input(f'Enter the rainfall in inches for {month} {year}: '))
                except ValueError:
                    print('Please enter a valid number')
                    rainfall = float(input(f'Enter the rainfall in inches for {month} {year}: '))
                self.rainfall.append(rainfall)
                self.total_rainfall += rainfall
                self.total_months += 1
        self.average_rainfall = self.total_rainfall / self.total_months

    def print_rainfall(self):
        print(f'The total number of months is {self.total_months}')
        print(f'The total rainfall is {self.total_rainfall} inches')
        print(f'The average rainfall per month is {self.average_rainfall} inches')

def run_collector():
    rainfall = RainfallCollector()
    rainfall.get_rainfall()
    rainfall.print_rainfall()

if __name__ == '__main__':
    run_collector()


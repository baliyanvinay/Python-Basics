# Named Tuple
from collections import namedtuple

Car = namedtuple(typename='Car', field_names='brand, model, year')
first_car = Car(brand='Tata', model='Altorz', year=2018)
second_car = Car('Kia', model='Sonet', year=2021)
third_car = Car('Hyundai', 'i20', 2020)

car_list = [first_car, second_car, third_car]

for car in car_list:
    print(car)


# Default Dict
from collections import defaultdict

motor_bike = {'brand': 'RE', 'model': 'Classic 350', 'year': 2019}

try:
    print(motor_bike['color'])
except KeyError as error_msg:
    print(f"KeyError: Not present {error_msg} in Motor Bike")    

motor_bike = defaultdict(lambda: 'Stormrider Sand') # default value for all missing keys
motor_bike['brand'] = 'RE'
motor_bike['model'] = 'Storm Rider Sand'
motor_bike['year'] = 2019

print(motor_bike['color']) # will print default value

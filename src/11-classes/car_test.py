from car import Car , ElectricCar as EC

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())
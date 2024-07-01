class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand  # __ is used to make a variable private
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_discription():
        return "Cars are amazing!"

    @property
    def model(self):
        return self.__model()


class electric_car(Car):
    def __init__(self, brand, __model, battery_size):
        super().__init__(brand, __model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_electric_car = electric_car("Tesla", "Model s", "85kw")
# print(my_electric_car.full_name())
# # print(my_electric_car.__brand)
# print(my_electric_car.get_brand())
# print(my_electric_car.fuel_type())
# print(Car.total_car)


my_car = Car("Volvswagen", "Virtus")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(Car.total_car)
# print(Car.general_discription())


my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

# my_car.model = "city"

# print(my_car.model())

# print(isinstance(my_electric_car, Car))
# print(isinstance(my_electric_car, electric_car))

class Battery(Car):
    def battery_info(self):
        return "This is battery"

class Engine(Car): 
    def engine_info(self):
        return "This is engine"  

class electric_car_two(Battery,Engine,Car):
    pass

my_new_electric_car = electric_car_two("tesla","S model")

print(my_new_electric_car.battery_info())
print(my_new_electric_car.engine_info())
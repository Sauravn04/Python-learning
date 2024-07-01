class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


class electriccartwo(Battery, Engine):
    pass

my_new_car = electriccartwo("Tesla", "S model")

print(my_new_car.battery_info())
print(my_new_car.engine_info())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print("Brand: " + self.brand)
        print("Model: " + self.model)
        print("Year: " + self.year)

car1 = Car("BMW", "v8", "2019")
car2 = Car("AUDI", "b4", "2934")
car3 = Car("NISSAN", "juke", "2000")

car1.print_car_info()
print(f"___")
car2.print_car_info()
print(f"___")
car3.print_car_info()
print(f"___")
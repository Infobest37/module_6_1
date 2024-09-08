class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info_display(self):
        print(f' Автомобиль {self.make} {self.model} {self.year}')
    def total_info_car(self):
        print(f" Автомобиль {self.make} {self.model} {self.year} не имеет ни какой батареи")


class ElecticCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def info_bettery_display(self):
        print(f" Емкость батареи {self.battery_size} кВТ.ч")

    def total_info_car(self):

        print(f" Автомобиль {self.make} имееет батарею {self.battery_size}, {self.model}, {self.year}")





car = Car('Camry', "ve3",1996)
car.info_display()
car2 = ElecticCar('Tesla', "Model S",2022, 2000)
car2.info_bettery_display()
car.total_info_car()
car2.total_info_car()

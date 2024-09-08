class Dog:
    def song(self):
        return "Гаф"

class Cat:
    def song(self):
        return "Мяу"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.song())


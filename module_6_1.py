class Animals:


    def __init__(self, name):
        self.name = name
        self.alive = True # живое существо
        self.fed = False # True Сытый или  False голодный


class Plant:


      def __init__(self, name):
        self.name = name
        self.edidle = False # Проверяем съедобно или нет False не съедобно True съедобно

class Predator(Animals):

    def eat(self, food):
        if food.edidle == False: # проверка на съедобность
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")
class Mammal(Animals):
    def eat(self, food):
        if food.edidle == False: # проверка на съедобность
            self.fed = True
            print(f"{self.name} съел {food.name}")
class Flower(Plant):
     def food(self, name):
        super().__init__(name)
        self.edible = False  # Цветы не съедобные


class Fruit(Plant):
    def food(self, name):
        super().__init__(name)
        self.edidle = True # Фрукты съедобные



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
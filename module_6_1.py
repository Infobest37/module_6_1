class Animals:


    def __init__(self, name):
        self.name = name
        self.alive = True # живое существо
        self.fed = False # True Сытый или  False голодный


class Plant:

       # Проверяем съедобно или нет False не съедобно True съедобно
      def __init__(self, name):
        self.name = name
        self.edidle = False

      def food(self, food):
          self.food = food

class Plant:
    def __init__(self, name, edible=False):  # добавляем параметр edible
        self.name = name
        self.edible = edible  # Проверяем съедобно или нет False не съедобно True съедобно


class Predator(Animals):
    def eat(self, food):
        if food.edible:  # Проверяем съедобность еды
            self.fed = True # Животное сыто
            print(f'{self.name} съел {food.name} и погиб')
        else:
            self.alive = False  # Если еда несъедобная - животное умирает
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animals):
    def eat(self, food):
        if food.edible:  # Проверяем съедобность еды
            self.fed = True # Животное сыто
            print(f'{self.name} съел {food.name} и насытился.')
        else:
            self.alive = False # Если не поел - животное умирает
            print(f'{self.name} не стал есть {food.name} и погиб.')


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)  # Цветы не съедобные


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True) # Фрукты можно есть




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
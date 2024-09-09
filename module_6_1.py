class Animals:
    alive = True  # Живое существо
    fed = False  # True сытый, False голодный

    def __init__(self, name):
        self.name = name

    def eat(self, food: 'Plant'):  # Используем строковую аннотацию
        if food.edible:  # Проверка на съедобность
            print(f"{self.name} съел {food.name}")
            self.fed = True  # Животное сыто
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # Животное погибает


class Plant:
    edible = False  # По умолчанию растения несъедобные

    def __init__(self, name):
        self.name = name


class Predator(Animals):
    pass


class Mammal(Animals):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True  # Фрукты съедобные


# Примеры использования
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Животные пытаются есть растения
a1.eat(p1)  # Волк не ест цветы, они несъедобные
a2.eat(p2)  # Хатико ест апельсин

print(a1.alive)
print(a2.fed)

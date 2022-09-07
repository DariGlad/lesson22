# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, number, population):
        self.number = number
        self.population = population

    def get_person_room(self):
        return self.number

    def get_city_population(self):
        return self.population


# TODO после выполнения задания попробуйте
person_1 = Person(42, 100500)
print(
    person_1.get_person_room(),
    person_1.get_city_population(),
    sep="\n"
)
# сделать экземпляр класса person и вызвать новые методы.

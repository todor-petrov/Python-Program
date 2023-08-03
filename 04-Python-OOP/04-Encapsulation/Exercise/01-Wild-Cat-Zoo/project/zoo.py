from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif self.__budget < price:
            return f'Not enough budget'
        return f'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        w = next((w for w in self.workers if w.name == worker_name), None)
        if w and w in self.workers:
            self.workers.remove(w)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_money = sum([w.salary for w in self.workers])
        if self.__budget < needed_money:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= needed_money
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        needed_money = sum([a.money_for_care for a in self.animals])
        if self.__budget < needed_money:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= needed_money
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        if lions:
            result.append(f'----- {len(lions)} Lions:')
            for lion in lions:
                result.append(lion.__repr__())
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        if tigers:
            result.append(f'----- {len(tigers)} Tigers:')
            for tiger in tigers:
                result.append(tiger.__repr__())
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        if cheetahs:
            result.append(f'----- {len(cheetahs)} Cheetahs:')
            for cheetah in cheetahs:
                result.append(cheetah.__repr__())
        nl = '\n'
        return nl.join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        if keepers:
            result.append(f'----- {len(keepers)} Keepers:')
            for keeper in keepers:
                result.append(f'{keeper.__repr__()}')
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        if caretakers:
            result.append(f'----- {len(caretakers)} Caretakers:')
            for caretaker in caretakers:
                result.append(f'{caretaker.__repr__()}')
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        if vets:
            result.append(f'----- {len(vets)} Vets:')
            for vet in vets:
                result.append(f'{vet.__repr__()}')
        nl = '\n'
        return nl.join(result)


zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),
Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1),
Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95),
Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),
Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
# Adding all animals
for i in range(len(animals)):
 animal = animals[i]
 price = prices[i]
 print(zoo.add_animal(animal, price))
# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
    # Tending animals
print(zoo.tend_animals())
# Paying keepers
print(zoo.pay_workers())
# Fireing worker
print(zoo.fire_worker("Adam"))
# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

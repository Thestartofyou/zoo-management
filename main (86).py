class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print(f"{animal.name} is not in the {self.name}.")

    def list_animals(self):
        print(f"Animals in {self.name}:")
        if self.animals:
            for animal in self.animals:
                print(f"Name: {animal.name}, Species: {animal.species}, Age: {animal.age}")
        else:
            print("No animals in the zoo.")

# Example usage
zoo = Zoo("Central Zoo")

# Adding animals to the zoo
lion = Animal("Simba", "Lion", 5)
zoo.add_animal(lion)

elephant = Animal("Jumbo", "Elephant", 10)
zoo.add_animal(elephant)

g

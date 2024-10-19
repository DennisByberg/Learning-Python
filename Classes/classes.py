class Animal:
    def __init__(self, type_of_animal, age):
        self.type_of_animal = type_of_animal
        self.age = age

    def __eq__(self, value) -> bool:
        return self.type_of_animal == value.type_of_animal and self.age == value.age

    def __gt__(self, value):
        return self.type_of_animal > value.type_of_animal and self.age > value.age

    def __add__(self, value):
        return Animal(self.type_of_animal + value.type_of_animal, self.age + value.age)

    @classmethod
    def zero(cls):
        return cls("Animal", 0)

    def make_sound(self):
        print(f"The {self.type_of_animal} makes a sound")

    def get_age(self):
        return self.age


cat = Animal("Cat2", 6)
cat2 = Animal("Cat", 5)

print(cat + cat2)

combined = cat + cat2
print(combined.age)


dog = Animal.zero()

dog.make_sound()
cat.make_sound()
print(cat.get_age())

class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def __init__(self, breed):
        self._breed = breed

    def speak(self):
        print(f"The {self._breed} barks")

    def print_breed(self):
        print(f"this dog is a {self._breed}")

    def describe(self):
        print(f"This is a {self._breed} dog")


class Cat(Animal):
    def __init__(self, color):
        self._color = color

    def speak(self):
        print(f"the {self._color} cat meows")

    def describe(self):
        print(f"This is a {self._color} cat")


dog = Dog("Golden Retriever")
cat = Cat("White")

dog.speak()
dog.describe()

cat.speak()
cat.describe()

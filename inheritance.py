class Animal:

    race = ""
    gender = ""
    age = 0

    def __init__(self, race, gender, age):
        self.race = race
        self.gender = gender
        self.age = age

    def printName(self):

        print("race is: " + self.race)


class Dog(Animal):
    paw_size = 0

    def __init__(self, paw_size, race, age, gender):

        super().__init__(race, gender, age)
        self.paw_size = paw_size

    def printName(self):
        super().printName()


dog1 = Dog(10, "Dackel", "male", 5)

dog1.printName()

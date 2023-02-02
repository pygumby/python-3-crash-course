class Person:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def get_name(self):
        print("The name of this person is:", self.name)

    def speak(self):
        print(f"Feed me more {self.food.lower()}s.")

    def __str__(self):
        return self.name

lucas = Person("Lucas", 31, "Burger")

print(lucas)
print(type(lucas))

lucas.get_name()
lucas.speak()

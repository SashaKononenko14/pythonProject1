class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.is_sleeping = False
        self.hunger_level = 5

    def sleep(self):
        self.is_sleeping = True

    def eat(self):
        if self.is_sleeping:
            print(f"{self.name} заснув і не може їсти!")
        else:
            self.hunger_level -= 1
            print(f"{self.name} поїв. Рівень голоду: {self.hunger_level}")

    def play(self):
        if self.is_sleeping:
            print(f"{self.name} заснув і не може гратися!")
        else:
            print(f"{self.name} грається!")

    def __str__(self):
        return f"Котик {self.name}, {self.age} років, порода: {self.breed}"
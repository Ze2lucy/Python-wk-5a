
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to fight crime!"


class Villain(Superhero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.__evil_plan = evil_plan

    def introduce(self):
        return f"I am {self.name}, and {self.city} will be mine! 😈"

    def reveal_plan(self):
        return f"{self.name}'s evil plan is: {self.__evil_plan}"

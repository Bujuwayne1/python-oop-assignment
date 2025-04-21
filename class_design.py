class Superhero:
    def __init__(self, name, power):
        self.name = name    # Encapsulated attributes
        self.power = power

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

class Villain(Superhero):  # Inheritance
    def __init__(self, name, power, evil_plan):
        super().__init__(name, power)  # Initialize parent class
        self.evil_plan = evil_plan    # Child-specific attribute

    def reveal_plan(self):            # Child-specific method
        print(f"{self.name}'s evil plan: {self.evil_plan}")

# Usage
hero = Superhero("Thor", "lightning")
villain = Villain("Loki", "illusions", "rule Asgard")

hero.use_power()       # Output: "Thor uses lightning!"
villain.reveal_plan()  # Output: "Loki's evil plan: rule Asgard"

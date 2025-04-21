class Animal:
    def move(self):
        pass  # Abstract method

class Bird(Animal):
    def move(self):    # Polymorphism: Override parent method
        print("Flying")

class Fish(Animal):
    def move(self):    # Polymorphism: Override parent method
        print("Swimming")

# Usage
animals = [Bird(), Fish()]
for animal in animals:
    animal.move()  # Output: "Flying" → "Swimming"

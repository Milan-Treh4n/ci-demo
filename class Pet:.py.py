class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        if self.species.lower() == "dog":
            return f"{self.name} says: Woof!"
        elif self.species.lower() == "cat":
            return f"{self.name} says: Meow!"
        else:
            return f"{self.name} makes a sound."

# Example usage:
if __name__ == "__main__":
    my_pet = Pet("Buddy", "Dog")
    print(my_pet.speak())
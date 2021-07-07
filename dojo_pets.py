
import pets


class Ninja:
    def __init__(self, firstName, lastName, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = 10
        self.petFood = 10
        self.pet = pet()

    def walk(self):
        print(f'you take {self.pet.Name} for a walk')
        self.pet.play()

    def feed(self):
        print(f'you give {self.pet.Name} some food')
        self.pet.eat()

    def bathe(self):
        print(f"you give {self.pet.Name} a bath, they don't like it")
        self.pet.noise()


jacob = Ninja('jacob', 'johnson', pets.dog)
jacob.pet.nameYourPet('muddy')
jacob.walk()
jacob.feed()
jacob.bathe()
print(jacob.pet.health)
print(jacob.pet.energy)
print(jacob.pet.type)

logan = Ninja('logan', 'lucas', pets.cat)
logan.pet.nameYourPet('jack')
logan.walk()
logan.feed()
logan.bathe()
print(logan.pet.health)
print(logan.pet.energy)
print(logan.pet.type)

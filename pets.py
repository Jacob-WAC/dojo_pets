class Pet:
    def __init__(self, Name='cat',  tricks=['fetch', 'roll over']):
        self.Name = Name
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(f"{self.Name} {self.petNoise}")

    def nameYourPet(self, name):
        self.Name = name


class cat(Pet):
    def __init__(self, Name="name"):
        super().__init__(Name)
        self.type = "cat"
        self.tricks = "lays down"
        self.petNoise = 'meows'


class dog(Pet):
    def __init__(self, Name="name"):
        super().__init__(Name)
        self.type = "dog"
        self.tricks = "fetch"
        self.petNoise = 'woofs!'

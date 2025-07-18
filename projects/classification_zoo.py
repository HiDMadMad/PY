class animal():
    zoo_name = 'islamic republic'

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        print(f'your {self.species} was added.')

    def make_sound(self):
        return self.sound
    
    def info(self):
        return f'\nname : {self.name}\nspecies : {self.species}\nage : {self.age}\nsound : {self.sound}'
    
    def __str__(self):
        return f'\nname : {self.name}\nspecies : {self.species}\nage : {self.age}\nsound : {self.sound}'


class bird(animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
    
    def info(self):
        return f'\nname : {self.name}\nspecies : {self.species}\nage : {self.age}\nsound : {self.sound}\nwing span : {self.wing_span}'
    
    def __str__(self):
        return f'\nname : {self.name}\nspecies : {self.species}\nage : {self.age}\nsound : {self.sound}\nwing span : {self.wing_span}'

    def __len__(self):
        return self.wing_span
#MadMad_34
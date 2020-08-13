import datetime
import random

class Person:
    name = ""
    birthday = "1/1/1111"
    created = datetime.datetime.now()
    person_id = 1

    def __init__ (self, name, birthday):
        self.name = name
        self.birthday = birthday

class User(Person):
    strength = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    dexterity = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    constitution = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    intelligence = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    wisdom = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    luck = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    def __init__ (self, name, birthday):
        Person.__init__(self, name, birthday)
            
class NPC(Person):
    
    def __init__(self, name, birthday, occupation):
        Person.__init__(self, name, birthday)
        self.job = occupation

Angel = User("Angel Padilla", "7/17/1995")

Rob = NPC("Robert Neggle", "7/24/1995", "Blacksmith")

print(Angel.strength)

print(Rob.name  + " works as a " + Rob.job)

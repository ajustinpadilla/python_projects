from abc import ABC, abstractmethod
import random

class weapon(ABC):
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.dmg = damage

    @abstractmethod
    def attack(self, dmg_type):
        pass

class sword(weapon):
    
    def attack(self, dmg_type):
        dmg = random.randint(0,10) + self.dmg
        print("Your {} slash at your foe dealing {} {} damage".format(self.name, dmg, dmg_type))


if __name__ == "__main__":
    excalibur = sword("Excalibur", 200, 10)
    excalibur.attack("slashing")
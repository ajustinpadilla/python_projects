import math

class vehicle:
    name = "Unkown Vehicle"
    person_cap = 1
    dis_unit = "miles"
    speed_unit ="mph"

    def __init__(self, name, load_cap = 25,  land_speed = 20):
        self.name = name
        self.load_cap = load_cap
        self.land_speed = land_speed

    def move(self):
        distance = int(input("\nYour {} moves at {} {}.\nHow many {} are you moving in/on your {}?\n>>>".format(self.name, self.land_speed,self.speed_unit, self.dis_unit, self.name)))
        hours = math.trunc(distance / self.land_speed)
        minutes = math.trunc(((distance / self.land_speed) - hours) * 60)
        if(hours > 1):
            print("\nIt took {} hours and {} minutes to travel {} {} on your {}.".format(hours, minutes, distance, self.dis_unit, self.name))
        elif(hours == 1 and minutes > 0):
            print("\nIt took {} hour and {} minutes to travel {} {} on your {}.".format(hours, minutes, distance, self.dis_unit, self.name))        
        else:
            print("\nIt took {} minutes to travel {} {} on your {}.".format(minutes, distance, self.dis_unit, self.name))

class boat(vehicle):
    dis_unit = "knots"
    speed_unit = "knots per hour"

class plane(vehicle):
    air_speed = 550

    def __init__(self, name, load_cap = 307000, land_speed = 160):
        self.name = name
        self.load_cap = load_cap
        self.land_speed = land_speed
    
    def move(self):
        terrain = input("Are you traveling through the air or on the ground? (air/ground)\n>>>").lower()
        while(terrain != "air" and terrain != "ground"):
            print("Please input air or ground!")
            terrain = input("Are you traveling through the air or on the ground? (air/ground)\n>>>").lower()
        if(terrain == "ground"):
            super().move()
        if(terrain == "air"):
            distance = int(input("\nYour {} moves at {} {}.\nHow many {} are you moving in/on your {}?\n>>>".format(self.name, self.air_speed,self.speed_unit, self.dis_unit, self.name)))
            hours = math.trunc(distance / self.air_speed)
            minutes = math.trunc(((distance / self.air_speed) - hours) * 60)
            if(hours > 1):
                print("\nIt took {} hours and {} minutes to travel {} {} on your {}.".format(hours, minutes, distance, self.dis_unit, self.name))
            elif(hours == 1 and minutes > 0):
                print("\nIt took {} hour and {} minutes to travel {} {} on your {}.".format(hours, minutes, distance, self.dis_unit, self.name))        
            else:
                print("\nIt took {} minutes to travel {} {} on your {}.".format(minutes, distance, self.dis_unit, self.name))

        



boaty = plane("747")

boaty.move()

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
    engine_type = "sail"
    anchored = True
    def move(self):
        if(self.anchored):
            print("\nCannot move {} because it is anchored. Please unanchor {}".format(self.name, self.name))
            self.moveAnchor()
        else:
            super().move()
            nextOption = input("\nWould you like to anchor now or move more?(anchor/move/end)\n>>>").lower()
            while(nextOption != "anchor" and nextOption != "move" and  nextOption != "end"):
                print("\nPlease answer with anchor, move, or end!!")
                nextOption = input("\nWould you like to anchor now or move more?(anchor/move/end)\n>>>").lower()
            if(nextOption == "anchor"):
                self.moveAnchor()
            if(nextOption == "move"):
                self.move()
            else:
                pass
    def moveAnchor(self):
        if(self.anchored):
            anchor_position = input("\nWould you like to pull the anchor up?(yes/no)\n>>>").lower()
            while(anchor_position != "yes" and anchor_position != "no"):
                print("\nPlease answer with yes or no!")
                anchor_position = (input("\nWould you like to pull the anchor up?(yes/no)\n>>>")).lower()
            if(anchor_position == "yes"):
                print("Your anchor has been pulled up. you may now sail {}.".format(self.name))
                self.anchored = False
                self.move()
            elif(anchor_position == "no"):
                print("\nYour {} will stay anchored. You cannot sail.".format(self.name))
        else:
            anchor_position = input("\nwould you like to anchor your {}.(yes/no)\n>>>".format(self.name)).lower()
            while(anchor_position != "yes" and anchor_position != "no"):
                print("\nPlease answer with yes or no!")
                anchor_position = input("\nWould you like to pull the anchor up?(yes/no)\n>>>").lower()
            if(anchor_position == "yes"):
                print("Your anchor has been let down. You cannot sail {}.".format(self.name))
                self.anchored = True
            elif(anchor_position == "no"):
                print("\nYour {}'s anchor will stay up.\n you may sail {}".format(self.name, self.name))
                self.move()

class plane(vehicle):
    air_speed = 550
    engine_type = "General Electric GEnx"

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

        



boaty = boat("boaty")

boaty.move()

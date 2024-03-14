# this is a class that describes cars
class car:
 def __init__ (self ,model,make,year_of_production,fuel_capacity,colour,horse_power):
    self.model = model 
    self.make = make
    self.year_of_production = year_of_production
    self.fuel_capacity = fuel_capacity
    self.colour = colour
    self.horse_power = horse_power

print("The car is of{0} make".format (self.make))    
    

my_car = car("Impalla","chevrolet","1969","lilac","2500cc",)  

my_car.print_make("chevrolet")
 
def set_make(self,make):
    self.make = make

def get_make(self):
         return self.make


def set_colour(self,colour):
    self.colour = colour

def get_colour(self):
         return self.colour


print (my_car.set_make())


class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def myLocation(self):
        print("Hi, my name is "+ self.name + " and I live in "+ self.country + ".")

loc = Location("Jason Elington", "Indonesia")
print(loc.name)
print(loc.country)

print(type(loc))
print("------------")
loc2 = Location("Jason Elington", "Indonesia")
loc2.myLocation()
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
loc2 = Location("Tomas", "Portugal")
loc2.myLocation()

loc3 = Location("Ying", "China")
loc4 = Location("Amare", "Kenya")

loc3.myLocation()
loc4.myLocation()

your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()

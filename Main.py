from Planetarium import Planetarium

planetarium1 = Planetarium()
planetarium1.create()

print("1, Mercury \n")
print("2, Venus \n")
print("3, Earth \n")
print("4, Mars \n")
print("5, Jupiter \n")
print("6, Saturn \n")
print("7, Uranus \n")
print("8, Neptune \n")

menu = int(input("Choose: "))

print(planetarium1.planets[menu - 1])

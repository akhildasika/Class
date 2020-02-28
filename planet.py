class Planet(object):
    names = ["Mercury","Venus","Earth","Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    diameters = ["3031.9", "7520.8", "7917.5", "4212.3","86881", "72367", "31518", "30599"]
    distances = ["1st","2nd","3rd","4th","5th","6th","7th","8th"]
    def __init__(self, name, diameter, distance):
        self.nameIndex = name
        self.diameterIndex = diameter
        self.distanceIndex = distance
        
    def __str__(self):
        name=Planet.names[self.nameIndex]
        diameter=Planet.diameters[self.diameterIndex]
        distance=Planet.distances[self.distanceIndex]
        return "Planet: "+ name + ", " + "Diameter: " + diameter + " mi, " + distance + " from Sun"
    

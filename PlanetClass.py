
class Planet(object):
    size = []
    description = []


    def_init_(self, size, description):
        self.sizeIndex = size
        self.descriptionIndex = description

    def_str_(self):
        size = Planet.sizes[self.sizeIndex]
        description = Planet.description[self.descriptionIndex]
        return size + description

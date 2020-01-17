class City:
    def __init__(self, name, mayor, year_established):
        self.name = name
        self.mayor = mayor
        self.year_established = year_established
        self.buildings = list()

    def add_building(self, building):
        self.buildings.append(building)

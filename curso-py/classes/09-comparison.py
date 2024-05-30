class Coordinates:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon

    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon

    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coords = Coordinates(45, 27)
coords2 = Coordinates(45, 27)
# This gives us "False" because they are instances that occupy different places in the RAM
# print(coords == coords2)

print(coords >= coords2)


class Node:
    parent = 0
    def __init__(self, city, g, h):
        self.city = city
        self.g = g
        self.h = h
        self.f = g + h

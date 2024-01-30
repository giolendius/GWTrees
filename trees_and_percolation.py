from random import uniform
from random import randint


def bernoulli(p):
    a = uniform(0, 1)
    if p > a:
        return 1
    else:
        return 0


def rdsq(length, min_int, max_int):
    a = []
    for i in range(length):
        a.append(randint(min_int, max_int))
    return a


class Point:
    def __init__(self, parent_point, son_number):  # first is Point type or None, second is int
        self.parent = parent_point
        self.son_number = son_number
        if parent_point is None:
            self.name = 'R'
        else:
            self.name = parent_point.name + str(son_number)
        if parent_point is None:
            self.gen = 0
        else:
            self.gen = len(self.parent.name)
        self.field = 2


class Tree:
    def __init__(self, sequence):
        R = Point(None, 0)
        self.potential = [R]
        self.points = [R]
        self.lastgen = []
        self.died = False

        for children in sequence:
            pr = self.potential[0]
            if children != 0:
                for child in range(1, children+1):
                    x = Point(pr, child)  # x is temporary a point
                    self.potential += [x]
                    self.points += [x]
                    # self.gen1.append(self.potentialNames[0] + str(child))
            self.died = len(self.potential) == 1
            if self.died:
                break
            del (self.potential[0])

        for point in self.points:
            if point.gen == self.points[-1].gen:
                self.lastgen.append(point)

    def printallpoints(self):
        for point in self.points:
            print(point.name)

    def ancestorline_points(self, point):
        ancline = []
        current = point
        for i in range(len(point.name)):
            ancline.append(current)
            current = current.parent
        return ancline

    
    def ancestorline_names(self, point):
        ancline = []
        current = point
        for i in range(len(point.name)):
            ancline.append(current.name)
            current = current.parent
        return ancline

    def generate_field(self, parameter):
        if self.died is False:
            for point in self.points:
                point.field = bernoulli(parameter)

    def print_field(self):
        for point in self.points:
            print(f'Point {point.name}, field {point.field}')

    def percolation(self):
        if self.died is True:
            return 'Tree died. Perc. not def.'
        for point in self.lastgen:
            a = 1
            for vertex in self.ancestorline_points(point):
                a *= vertex.field
            if a == 1:
                return f"Percolation succeed from root to leaf {point.name}"
        return "No percolation"

from random import uniform
from random import randint


def bernoulli(p):
    a = uniform(0, 1)
    if p > a:
        return 1
    else:
        return 0


def rdsq(length: int, min_int: int, max_int: int) -> list[int]:
    f"Returns a list of {length} integers randomly chossen between {min_int} and {max_int}"
    return [randint(min_int, max_int) for i in range(length)]


class Point:
    """Creates a Point object,  with a parent point and a child tag which represent the number of "older" sibling  +1"""

    def __init__(self, parent_point: "Point", son_number: int):
        self.parent = parent_point
        self.son_number = son_number
        self.name = ""
        if parent_point == None:
            self.name = 'R'
        else:
            self.name = parent_point.name + str(son_number)
        if parent_point == None:
            self.gen = 0
        else:
            self.gen = len(self.parent.name)
        self.field = 3


class Tree:
    def __init__(self, sequence: list):
        R = Point(None, 0)
        self.potential = [R]
        self.points = [R]
        self.last_gen = []
        self.died = False

        for children in sequence:
            parent = self.potential[0]
            if children != 0:
                for child in range(1, children + 1):
                    x = Point(parent, child)
                    self.potential += [x]
                    self.points += [x]
            self.died = len(self.potential) == 1
            if self.died:
                break
            del (self.potential[0])

        for point in self.points:
            if point.gen == self.points[-1].gen:
                self.last_gen.append(point)

    def printallpoints(self):
        for point in self.points:
            print(point.name)

    def ancestorline(self, point: Point, only_points_names: bool):
        ancline = []
        current = point
        for i in range(len(point.name)):
            if only_points_names:
                ancline.append(current.name)
            else:
                ancline.append(current)
            current = current.parent
        return ancline

    def generate_field(self, parameter: float):
        if not self.died:
            for point in self.points:
                point.field = bernoulli(parameter)
    def print_field(self):
        for point in self.points:
            print(f'Point {point.name}, field {point.field}')

    def percolation(self):
        if self.died:
            return 'Tree died. Percr. not def.'
        for point in self.last_gen:
            a = 1
            for vertex in self.ancestorline(point, False):
                a *= vertex.field
            if a == 1:
                return f"Percolation succeed from root to leaf {point.name}"
        return "No percolation"

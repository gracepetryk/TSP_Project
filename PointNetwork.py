""""
Author: Grace Petryk

Simple class encoding the network of points into a data structure
"""

import math


class PointNetwork:

    def __init__(self, file_name):

        # read file into list of strings
        with open(file_name, "r") as f:
            file_lines = f.readlines()

        self.numPoints = int(file_lines[0]) # read the first

        self.points = []
        for line in file_lines[1:]:
            # read every line after the first into a list of points
            point = line.split(' ')
            self.points.append((int(point[0]), int(point[1])))

    def find_length(self, point_order):
        """
        finds the total length of a given path
        """

        length = 0
        for i in range(0, self.numPoints - 1):
            length += find_distance(self.points[point_order[i]],
                                    self.points[point_order[i + 1]])
        return length

    def path_str(self, point_order):
        """
        :returns a string representation of a given path with the length on the first line and each point in order
        on subsequent lines
        """
        string_representation = ""
        string_representation += str(self.find_length(point_order)) + "\n"
        for i in point_order:
            point = self.points[i]
            string_representation += "{0} {1}\n".format(point[0], point[1])

        string_representation = string_representation[:-1]  # strip final newline by removing last character

        return string_representation

    def __str__(self) -> str:
        return "PointNetwork(numPoints: {0}, points: {1})".format(self.numPoints, self.points)


def find_distance(p1: (int, int), p2: (int, int)) -> float:
    """
    Finds the distance between two points in a network
    """

    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)







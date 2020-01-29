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
            self.points.append((point[0], point[1]))


def find_distance(p1: (int, int), p2: (int, int)) -> float:
    """
    Finds the distance between two points in a network
    """

    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

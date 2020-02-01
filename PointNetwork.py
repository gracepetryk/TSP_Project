""""
Author: Grace Petryk

Simple class encoding the network of points into a data structure
"""

import math
import typing
from typing import List, Tuple


class PointNetwork:

    points: List[Tuple[int, int]]

    def __init__(self, file_name):
        """
        Initializes the graph based on points defined in a file

        :param file_name: the file containing the point network, relative to working directory
        """

        # read file into list of strings
        with open(file_name, "r") as f:
            file_lines = f.readlines()

        self.numPoints = int(file_lines[0])  # read the first line for number of points

        self.points = []
        for line in file_lines[1:]:
            # read every line after the first into a list of points
            point = line.split(' ')
            self.points.append((int(point[0]), int(point[1])))

    def __str__(self) -> str:
        return "PointNetwork(numPoints: {0}, points: {1})".format(self.numPoints, self.points)


def find_distance(p1: (int, int), p2: (int, int)) -> float:
    """
    Finds the distance between two points in a network
    """

    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def find_length(points: typing.List[typing.Tuple[int, int]], point_order=None):
    """
    finds the total length of a given point order
    """

    if point_order is None:
        # if point order not specified, assume points are already in order
        point_order = range(0, len(points))

    length = 0
    for i in range(0, len(points) - 1):
        length += find_distance(points[point_order[i]],
                                points[point_order[i + 1]])
    return length





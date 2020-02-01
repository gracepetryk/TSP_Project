import PointNetwork
import sys


def find_nearest_neighbor_path(pn: PointNetwork.PointNetwork):
    path = [pn.points.pop()]

    while len(pn.points) > 0:
        current_point = path[-1]  # take the last point from the path as the current point

        best_distance = -1
        best_point_index = None

        for i in range(len(pn.points)):
            distance = pn.find_distance(current_point, pn.points[i])
            if best_distance < 0 or distance < best_distance:
                best_distance = distance
                best_point_index = i

        # swap last and best point and pop
        pn.points[-1], pn.points[best_point_index] = pn.points[best_point_index], pn.points[-1]
        path.append(pn.points.pop())

    return path

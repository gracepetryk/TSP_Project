import PointNetwork
import typing


def find_nearest_neighbor_path(pn: PointNetwork.PointNetwork) -> typing.List[typing.Tuple[int, int]]:

    # store a copy of the reversed point list, so that we start with the first item in the list
    points = pn.points[::-1]
    path = [points.pop()]

    while len(points) > 0:
        current_point = path[-1]  # take the last point from the path as the current point

        best_distance = None
        best_point_index = None

        for i in range(len(points)):
            distance = PointNetwork.find_distance(current_point, points[i])
            if best_distance is None or distance < best_distance:
                best_distance = distance
                best_point_index = i

        # swap last and best point and pop
        points[-1], points[best_point_index] = points[best_point_index], points[-1]
        path.append(points.pop())

    return path

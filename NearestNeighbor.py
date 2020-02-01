import PointNetwork
import typing


def find_nearest_neighbor_path(pn: PointNetwork.PointNetwork) -> typing.List[typing.Tuple[int, int]]:
    path = [pn.points.pop()] # start with the first point on the list

    while len(pn.points) > 0:
        current_point = path[-1]  # take the last point from the path as the current point

        best_distance = None
        best_point_index = None

        for i in range(len(pn.points)):
            distance = PointNetwork.find_distance(current_point, pn.points[i])
            if best_distance is None or distance < best_distance:
                best_distance = distance
                best_point_index = i

        # swap last and best point and pop
        pn.points[-1], pn.points[best_point_index] = pn.points[best_point_index], pn.points[-1]
        path.append(pn.points.pop())

    pn.points = path  # restore the point networks' point list

    return path

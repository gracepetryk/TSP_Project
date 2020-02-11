import PointNetwork
import typing


def find_nearest_neighbor_path(pn: PointNetwork.PointNetwork) -> typing.List[typing.Tuple[int, int]]:

    # store a copy of the point list, so that we start with the first item in the list
    path = [pn.points[0]]
    next_index = 1

    while next_index < len(pn.points):
        best_score = None
        best_index = 1
        for i in range(next_index, len(pn.points)):
            score = PointNetwork.find_distance(path[-1], pn.points[i])
            if best_score is None or score < best_score:
                best_score = score
                best_index = i

        path.append(pn.points[best_index])

        # swap best point and next point in list
        pn.points[next_index], pn.points[best_index] = pn.points[best_index], pn.points[next_index]

        # advance next
        next_index += 1

    return path

import PointNetwork
import typing


def exhaustive_search(pn: PointNetwork.PointNetwork) -> typing.List[typing.Tuple[int, int]] or None:
    """
    finds all n! permutations of points
    
    algorithm from https://www.topcoder.com/generating-permutations/ 

    :param pn: point network to search
    :return: the shortest path through the network
    """

    if pn.numPoints > 10:
        input_char = input("WARNING: This algorithm runs in O(n!) time. The current number of nodes is {0}, "
                           "this will take VERY long to run. Are you sure you want to continue? [y/N]: "
                           .format(pn.numPoints))
        if input_char.lower() != 'y':
            return None

    best_dict = {'path': [], 'distance': None}  # need to use a dict because inner functions cant modify outer vars

    def generate_permutations_recursive(n):
        points = pn.points

        if n == 1:
            distance = PointNetwork.find_length(points)
            if best_dict['distance'] is None or distance < best_dict['distance']:
                best_dict['distance'] = distance
                best_dict['path'] = points.copy()

        for i in range(0, n):
            points[n - 1], points[i] = points[i], points[n - 1]
            generate_permutations_recursive(n - 1)
            points[n - 1], points[i] = points[i], points[n - 1]

    generate_permutations_recursive(len(pn.points))
    return best_dict['path']

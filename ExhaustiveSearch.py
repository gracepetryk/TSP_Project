import PointNetwork
import typing


def generate_permutations(l: list) -> typing.List[typing.List[any]]:
    """
    finds all n! permutations of l

    :param l: list of items to find permutations of
    :return: all the permutations of l
    """
    if len(l) == 1:
        return [l]
    else:
        permutations = []

        # for each item in l, generate all the permutations of the list without and append the item to it
        # it then adds all these permutations to the master list

        for i in range(len(l)):
            item = l[i]

            # remove l[i] by swapping it with the last item of the list and popping, O(1)
            l[i], l[-1] = l[-1], l[i]
            l.pop()
            for perm in generate_permutations(l):  # generate all permutations of the list without that item
                perm.append(item)

                # need to add a copy of the perm because otherwise the references get all tangled and it stack overflows
                permutations.append(perm.copy())
                perm.pop()

            # reinsert the item by appending and swapping with item at i, O(1)
            l.append(item)
            l[i], l[-1] = l[-1], l[i]
        return permutations


def exhaustive_search(point_network: PointNetwork.PointNetwork) -> typing.List[typing.Tuple[int, int]]:
    index_permutations = generate_permutations(list(range(point_network.numPoints)))

    best_score = None
    best_path_indices = []

    for permutation in index_permutations:
        score = PointNetwork.find_length(point_network.points, permutation)

        if best_score is None or score < best_score:
            best_score = score
            best_path_indices = permutation

    #  translate list of indices into list of points
    best_path = []
    for i in best_path_indices:
        best_path.append(point_network.points[i])

    return best_path

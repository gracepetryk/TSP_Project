import sys
import PointNetwork
import typing


def generate_permutations(l: list) -> typing.List[typing.List[any]]:

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


def exhaustive_search(point_network: PointNetwork):
    index_permutations = generate_permutations(list(range(point_network.numPoints)))

    best_score = -1
    best_path = []

    for permutation in index_permutations:
        score = point_network.find_length(permutation)

        if best_score < 0:
            # handle first case
            best_score = score
            best_path = permutation
        else:
            if score < best_score:
                best_score = score
                best_path = permutation

    print(point_network.path_str(best_path))


print(generate_permutations([1, 2, 3]))

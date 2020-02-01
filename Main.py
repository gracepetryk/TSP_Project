import ExhaustiveSearch
import NearestNeighbor
import PointNetwork as pn
import argparse
import time
import typing

#############
# CONSTANTS #
#############

TIMING_PRECISION = 10
DISTANCE_PRECISION = 3


########################
# FUNCTION DEFINITIONS #
########################

def print_path(path: typing.List[typing.Tuple[int, int]]):
    distance = round(pn.find_length(path), DISTANCE_PRECISION)
    print(distance)
    for point in path:
        print("{0} {1}".format(point[0], point[1]))


##########################
# COMMAND LINE ARGUMENTS #
##########################

parser = argparse.ArgumentParser(description="Compares exhaustive and nearest neighbor searches for a given network")

parser.add_argument('-e', '--exhaustive', help='enables exhaustive search\n'
                                               'WARNING: this runs in O(n!) time, please use only networks '
                                               ' with n <= 10 nodes', action='store_true')
parser.add_argument('-n', '--nearest', help='enables nearest neighbor search', action='store_true')
parser.add_argument('-t', '--timing', help='enables timing', action='store_true')
parser.add_argument("FILE", help='the file where the network is stored')

args = parser.parse_args()


########
# MAIN #
########

point_network = pn.PointNetwork(args.FILE)

if args.exhaustive:
    exhaustiveStartTime = time.time()

    print_path(ExhaustiveSearch.exhaustive_search(point_network))

    exhaustiveTime = round(time.time() - exhaustiveStartTime, TIMING_PRECISION)

    if args.timing:
        print("Exhaustive search execution time: {0}s".format(exhaustiveTime))

    if args.nearest:
        print("\n")  # if nearest neighbors is also enabled print 2 newlines to separate

if args.nearest:
    nearestStartTime = time.time()

    print_path(NearestNeighbor.find_nearest_neighbor_path(point_network))

    nearestTime = round(time.time() - nearestStartTime, TIMING_PRECISION)

    if args.timing:
        print("Nearest Neighbor execution time: {0}s".format(nearestTime))


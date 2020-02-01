import sys
import random

num_nodes = int(sys.argv[1])

print(num_nodes)

for i in range(num_nodes):
    print("{0} {1}".format(random.randrange(100), random.randrange(100)))

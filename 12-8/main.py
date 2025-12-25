import math
from unionfind import UnionFind

def euclidean_dist(point1, point2):

    '''
    given point1 and point2 of form (X, Y, Z) 
    calculate euclidean distance between point1 and point2
    '''

    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)


points = []
TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'

def parse_line(line):
    return tuple(map(int, line.split(',')))

with open(INPUT_FILE, 'r') as file:
    for l in file:
        points.append(parse_line(l.strip()))

N = len(points)
dist = [[-1 for _ in range(N)] for _ in range(N)]  # dist[i][j] will represent dist between point i and point j

for i in range(N):
    for j in range(N):

        dist[i][j] = euclidean_dist(points[i], points[j])


# create a sorted list of distances
sorted_dist = []
for i in range(N):
    for j in range(i + 1, N):
        sorted_dist.append((dist[i][j], (i, j)))
sorted_dist.sort()

circuits = UnionFind(N)

for _, state in sorted_dist:
    i, j = state
    circuits.union(i, j)
    if circuits.is_all_merged():
        print(points[i][0] * points[j][0])
        break
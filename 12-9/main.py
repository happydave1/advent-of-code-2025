from typing import Tuple

TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'

def parse_line(line: str):
    p1, p2 = map(int, line.split(','))
    return (p1, p2)

def form_rectangle(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    s1 = abs(p1[0] - p2[0] + 1)
    s2 = abs(p1[1] - p2[1] + 1)
    return s1 * s2

points = []
with open(INPUT_FILE, 'r') as file:
    for l in file:
        points.append(parse_line(l.strip()))

N = len(points)
max_area = 0
for i in range(N):
    for j in range(i+1, N):
        cur_area = form_rectangle(points[i], points[j])
        # if cur_area > max_area:
        #     print(f"points {points[i]} and {points[j]} form the max area of {cur_area}")
        max_area = max(max_area, cur_area)
print(max_area)

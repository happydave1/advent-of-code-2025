import sys
from typing import Tuple, List
import bisect

INPUT_FILE = './input.txt'
TEST_FILE = './test.txt'

checking_fresh = False

def parse_range(line: str) -> Tuple[int, int]:
    '''
    given format lower-upper, return (lower, upper)
    '''

    lower, upper = map(int, line.split("-"))
    return lower, upper

def merge(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    '''
    go through a list of ranges which can overlap
    and make sure there is no overlap


    [(1, 5), (4, 6), (5, 6)] -> [(1, 6)]
    '''
    ranges.sort()
    merged = [ranges[0]]  # were gaurunteed to have ranges be truthy
    
    for lower, upper in ranges[1:]:
        cur_highest = merged[-1][1] 
        if lower <= cur_highest:
            merged[-1] = (merged[-1][0], max(cur_highest, upper))
        else:
            merged.append((lower, upper))

    return merged

def check_in_ranges(num: int, ranges: List[Tuple[int, int]]) -> bool:
    '''
    given a num, check if it is in a list of sorted ranges with no overlap
    '''

    # use binary search to find the closest range 
    closest_range_ind = bisect.bisect_left(ranges, (num, 0)) - 1
    # print(closest_range_ind)
    l, u =  ranges[closest_range_ind]
    return num >= l and num <= u

def check_total_of_ranges(ranges):
    total = 0
    for l, u in ranges:
        total += u - l + 1
    return total


ranges = []
total = 0

with open(INPUT_FILE, 'r') as file:

    
    for l in file:
    
        if l == '\n':            
            # begin checking fresh or not
            checking_fresh = True
            ranges = merge(ranges)

        elif not checking_fresh:
            lower, upper = parse_range(l.strip())
            ranges.append((lower, upper))
        
        elif checking_fresh:
            cur = int(l.strip())
            if check_in_ranges(cur, ranges):
                total += 1
        
        
print(total)

print(check_total_of_ranges(ranges))

# print(merge([(1, 5), (4, 6), (5, 6)]))  # [(1, 6)]
# print(check_in_ranges(3, [(1,6)]))  # True
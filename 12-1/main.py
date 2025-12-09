import requests
from typing import Tuple

# get the list from the input - stored as input.txt

INPUT_FILE_PATH = './input.txt'

### PART 1
def calculate_new_pos(pos: int, rotation: str) -> int:
    # given a pos and a rotation in the format LXXX or RXXX
    # where XXX is an integer, return the new position 

    direction = rotation[0]
    mag = int(rotation[1:])

    if direction == "L":

        if mag <= pos:
            return pos - mag

        remaining_mag = mag - pos  # make it point to 0 first
        remaining_mag %= 100  # eliminate unnecessary rotations
        return (100 - remaining_mag) % 100


    else:

        if pos + mag <= 100:
            return (pos + mag) % 100

        remaining_mag = mag - (100 - pos)
        remaining_mag %= 100
        return remaining_mag


### PART 2
def calculate_new_pos_and_count_zeros(pos: int, rotation: str) -> Tuple[int, int]:

    direction = rotation[0]
    mag = int(rotation[1:])

    # if we start at 0 simply return the mag // 100 
    if pos == 0:
        total_clicks = mag // 100
        rm = mag % 100
        new_pos = rm if direction == 'R' else (100 - rm)
        if new_pos == 0:
            total_clicks += 1
        return new_pos, total_clicks 

    if direction == "L":

        if mag <= pos:
            if mag == pos:
                return 0, 1
            else:
                return pos - mag, 0

        # we know mag > pos, we will cross 0 at least once
        remaining_mag = mag - pos  # make it point to 0 first
        total_clicks = 1
        total_clicks += remaining_mag // 100
        remaining_mag %= 100  # eliminate unnecessary rotations
        return (100 - remaining_mag) % 100, total_clicks


    else:

        if pos + mag <= 100:
            if pos + mag == 100:
                return (0, 1)
            else:
                return pos + mag, 0

        # we know that pos + mag > 100
        remaining_mag = mag - (100 - pos)
        total_clicks = 1
        total_clicks += remaining_mag // 100
        remaining_mag %= 100
        return remaining_mag, total_clicks

pos = 50
total = 0
with open(INPUT_FILE_PATH, "r") as file:
    for l in file:
        cur_rotation = l.strip()

        # pos = calculate_new_pos(pos, cur_rotation) # PART 1
        # pos, num_times_clicked_zero = calculate_new_pos_and_count_zeros(pos, cur_rotation)
        # total += num_times_clicked_zero
        # if pos == 0:
        #     total += 1

        pos, num_times_clicked_zero = calculate_new_pos_and_count_zeros(pos, cur_rotation)
        # print(f"for rotation {cur_rotation}, we see that it clicked zero {num_times_clicked_zero} times")
        total += num_times_clicked_zero

print(total)

# # TESTING 
# print(calculate_new_pos_and_count_zeros(50, 'L68'))
# print(calculate_new_pos_and_count_zeros(82, 'L30'))
# print(calculate_new_pos_and_count_zeros(52, 'R48'))
# print(calculate_new_pos_and_count_zeros(0, 'L5'))
# print(calculate_new_pos_and_count_zeros(0, 'R1000'))
# print(calculate_new_pos_and_count_zeros(50, 'R50'))  # (0, 0)
# print(calculate_new_pos_and_count_zeros(50, 'R1000'))



import sys
from typing import Callable

INPUT_FILE = "./input.txt"
TEST_FILE = "./test.txt"

def max_joltage(battery: str) -> int:

    # assumes we can only turn on 2 batteries

    # for the first digit, find the max of the battery which is not the last one
    # if there is a tie, break it by using the first occurrence

    # for the second digit, perform the same logic but limit the search space to the
    # location of the first digit to the end of the battery
    battery = list(battery)
    for i in range(len(battery)):
        battery[i] = int(battery[i])
    
    N = len(battery)
    first_digit = max(battery[:N-1])  # exclude last digit from search of first digit
    first_digit_ind = battery.index(first_digit)

    second_digit = max(battery[first_digit_ind + 1:])
    return int(''.join([str(first_digit), str(second_digit)]))

def max_joltage_2(battery: str) -> int:

    # convert battery to a list of ints
    battery = list(battery)
    for i in range(len(battery)):
        battery[i] = int(battery[i])


    temp = []
    N = len(battery)
    last_digit_ind = 0
    
    for i in range(12):
        
        last_digit_buffer = 11 - i
        scope = battery[last_digit_ind : N - last_digit_buffer]
        cur_digit = max(scope)

        cur_digit_ind = scope.index(cur_digit) + last_digit_ind
        last_digit_ind = cur_digit_ind + 1
        temp.append(cur_digit)
    
    temp = map(str, temp)
    return int(''.join(temp))
    


def run_func(part_function: Callable[[str], int], dataset: str = "input", debug: bool = False) -> None:
    if dataset == 'test':
        f = TEST_FILE
    else:
        f = INPUT_FILE
    total = 0
    with open(f, 'r') as file:
        for l in file:
            cur_battery = l.strip()
            
            j = part_function(cur_battery)
            
            if debug:
                print(f"for battery {cur_battery}, we find the max joltage of {j}")
            
            total += j

    print(total)



if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("enter the part after the script name (i.e. part1 or part2) and optionally which data to use (i.e. input or test)")
        sys.exit()

    else:
        part = sys.argv[1] 
        dataset = 'input' if len(sys.argv) == 2 else sys.argv[2]

        if part == "part1":

            run_func(max_joltage, dataset)
        
        elif part == "part2":
            
            run_func(max_joltage_2, dataset)
        
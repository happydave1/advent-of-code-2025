from typing import List

INPUT_FILE = './input.txt'
TEST_FILE = './test.txt'

def part_one(grid: List[List[str]]) -> int:
    N, M = len(grid), len(grid[0])
    totals_per_col = []   
    for col in range(M):
        operation = grid[-1][col]
        temp = 0 if operation == '+' else 1
        for row in range(N-1):
            cur = int(grid[row][col])
            if operation == '+':
                temp += cur
            elif operation == '*':
                temp *= cur
        
        totals_per_col.append(temp)
    
    return sum(totals_per_col)

def parse_col(col):
    '''
    given format ['328', '64', '98', '+'] -> ['328', '64x', '98x']

    328
    64
    98

    369 + 248 + 8 = 625

    '''
    operation = col[-1]
    col = col[:len(col) - 1]
    max_len = 0
    for el in col:
        max_len = max(max_len, len(el))

    # add padding to make it easier
    for i in range(len(col)):
        while len(col[i]) < max_len:
            t = list(col[i])
            t.append('x')
            col[i] = ''.join(t)

        # reverse each digit
        col[i] = ''.join(reversed(list(col[i])))

    digits = []
    for i in range(max_len):
        temp_digit = []

        for el in col:
            if el[i] != 'x':
                temp_digit.append(el[i])
        
        digits.append(int(''.join(temp_digit)))
    
    col_total = 0 if operation == '+' else 1
    for digit in digits:
        if operation == '+':
            col_total += digit
        elif operation == '*':
            col_total *= digit
    return col_total

def part_two(grid: List[List[str]]) -> int:
    '''
    given a grid representing the input, read each column 
    as a problem where grid[-1][col] represents the operation
    and the numbers are added in a right to left top down manner 
    '''

    N, M = len(grid), len(grid[0])
    totals = []

    for col in range(M):
        current_col = [row[col] for row in grid]
        totals.append(parse_col(current_col))
        print(current_col, parse_col(current_col))
    
    return sum(totals)

# check if all rows have same length
grid = []
with open(TEST_FILE, 'r') as file:
    for l in file:
        grid.append(l.strip().split())

# print(part_one(grid))
# print(parse_col(['328', '64', '98', '+']))

'''
328
64
98

8 + 248 + 369
'''
print(part_two(grid))
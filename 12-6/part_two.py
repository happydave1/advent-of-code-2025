
# retry part 2

TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'

raw_lines = []

with open(INPUT_FILE, 'r') as file:
    for line in file:
        raw_lines.append(line.rstrip('\n'))  

# for i in range(len(raw_lines)):
#     raw_lines[i] = ''.join(reversed(list(raw_lines[i])))

grid = [''.join(reversed(s)) for s in raw_lines]

# pad grid to the left 1 line of spaces
for i in range(len(grid)):
    grid[i] = grid[i] + ' '

# for l in grid:
#     # print(l)

# iterate over columns
totals = []
width = len(grid[0])
col_counter = 0
digits = []

operations = []
for o in grid[-1]:
    if o == '+' or o == '*':
        operations.append(o)


def is_blank(col):
    for c in col:
        if c != ' ':
            return False
    return True

for col in range(width):
    cur_col = [l[col] for l in grid]
    cur_operation = operations[col_counter]

    if is_blank(cur_col):
        # add total from previous column to totals array
        prev_total = 0 if cur_operation == '+' else 1
        if cur_operation == '+':
            totals.append(sum(digits))
        else:
            for d in digits:
                prev_total *= d
            totals.append(prev_total)

        # print(f"for col {col}, we are adding {prev_total} to the totals")
        # new column
        digits = []
        col_counter += 1
    
    else:
        # updating current column 
        # parse a digit
        cur_digit = int(''.join(cur_col[:len(cur_col) - 1]))
        digits.append(cur_digit)
        # print(f"for col {col} we see a digit of {cur_digit}")

print(sum(totals))
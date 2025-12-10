
grid = []

INPUT_FILE = './input.txt'
TEST_FILE = "./test.txt"

dirs = [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)]

def check_adj(i, j):
    adj = 0
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
            continue
        if grid[ni][nj] == '@':
            adj += 1
    return adj < 4


with open(TEST_FILE, 'r') as file:
    for l in file:
        grid.append(list(l.strip()))
    
total = 0
remove_list = []
keep_going = True
while keep_going:
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == '@' and check_adj(i, j):
                # print(f"for grid spot {i, j} we see that it works")
                remove_list.append((i, j))
                total += 1
    
    for ri, rj in remove_list:
        grid[ri][rj] = '.'
    keep_going = len(remove_list) > 0
    remove_list = []
print(total)
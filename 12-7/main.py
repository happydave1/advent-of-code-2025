

TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'

grid = []

with open(INPUT_FILE, 'r') as file:

    for l in file:
        grid.append(l.strip())

# VISUALIZING GRID
# for l in grid:
#     print(l)

N, M = len(grid), len(grid[0])
active_cols = [0 for _ in range(M)]
total = 0

for l in grid:

    for i in range(M):
        cell = l[i]
        if cell == 'S':
            active_cols[i] = 1
        elif cell == '^':
            if active_cols[i] == 1:
                active_cols[i] = 0
                if i - 1 >= 0: 
                    active_cols[i-1] = 1
                if i + 1 < M: 
                    active_cols[i+1] = 1
                total += 1

visited = set()
memo = {}

def dfs(cur_row, active_col):
    
    if cur_row >= N:
        return 1

    if active_col < 0 or active_col >= M:
        return 0

    state = (cur_row, active_col)

    if state in memo:
        return memo[state]

    if grid[cur_row][active_col] == '^':
        res = dfs(cur_row + 1, active_col + 1) + dfs(cur_row + 1, active_col - 1)
    else:
        res = dfs(cur_row + 1, active_col)
    
    memo[state] = res
    return res
    

start = -1
for i in range(len(grid[0])):
    if grid[0][i] == 'S':
        start = i

print(dfs(1, start))

print(total)                


'''
grid search problem:
There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible 
unique paths that the robot can take to reach the bottom-right corner.
'''


def grid_search(m: int, n: int) -> int:

    memo = {}
    def dfs(r, c):

        # base case
        if r == m - 1 and c == n - 1:
            return 1

        if r < 0 or r >= m or c < 0 or c >= n:
            return 0

        state = (r, c)
        if state in memo:
            return memo[state]

        res = dfs(r + 1, c) + dfs(r, c + 1)
        memo[state] = res
        return res
    
    return dfs(0, 0)

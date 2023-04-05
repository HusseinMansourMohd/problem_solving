#200. Number of Islands   Graph/BFS/DFS

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# 1/Initialize a variable count to store the number of islands.
# 2/Loop through each cell in the grid:
# a. If the current cell is '1', increment the count variable and perform DFS to mark all connected land cells as '0' (visited).
# b. Continue to the next cell.
# After traversing the entire grid, return the count variable as the number of islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'  #mark cell as visited

            #preform DFS on adjacent cells
            dfs(grid, row - 1 , col)
            dfs(grid, row + 1 , col)
            dfs(grid, row , col - 1)
            dfs(grid, row , col + 1)

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid,i,j)
        return count

        

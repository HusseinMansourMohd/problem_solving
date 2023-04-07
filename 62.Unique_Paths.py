class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP array with dimensions m x n, initialized to 1
        dp = [[1] * n for _ in range(m)]
        # Iterate through the grid starting from the second row and second column
        for i in range(1, m):
            for j in range(1, n):
            # The number of unique paths to cell (i, j) is the sum of unique paths to cells (i - 1, j) and (i, j - 1)
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

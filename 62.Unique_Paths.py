class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP array with dimensions m x n, initialized to 1
        dp = [[1] * n for _ in range(m)]
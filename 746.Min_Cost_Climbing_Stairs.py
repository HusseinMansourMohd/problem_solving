# 70. Climbing Stairs
# Easy
# 17.6K
# 546
# Companies
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        df = [0]*(len(cost)+1)
        df[0] = 0
        df[1] = cost[0]  #pay 10
        df[2] = cost[1] # pay 15

        for i in range(3,len(cost)+1):
            df[i] = min(df[i-1] + cost[i-1],df[i-2]) 

        return df[len(cost)]

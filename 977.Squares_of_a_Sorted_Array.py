#977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(0,len(nums)):
            new_nums.append(nums[i]*nums[i])
        return sorted(new_nums)
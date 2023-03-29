#977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(0,len(nums)):
            new_nums.append(nums[i]*nums[i])
        return sorted(new_nums)
    
#second solution:
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result
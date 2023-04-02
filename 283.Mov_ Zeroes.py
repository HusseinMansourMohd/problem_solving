class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeroes = 0
        left = 0
        right = len(nums) - 1
        output = []
        while len(output) + count_zeroes != len(nums):
            if left or right == 0:
                count_zeroes +=1
            if left < right:
                output.append(nums[left])
            elif right < left:
                output.append(nums[right])
            else:
                output.append(left)
                output.append(nums[right])
            if count_zeroes != 0:

                for i in range(count_zeroes):
                    output.append(0)
            nums = output
            
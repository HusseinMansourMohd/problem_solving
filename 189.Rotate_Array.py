#189. Rotate Array

class Solution:
    #####
    ####
    ###
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        
        """
        n = len(nums)
        k = k % n #module this for rotation
        self.reverse(nums, 0, n-1)#revese the whole array [6,5,4,3,2,1]
        self.reverse(nums, 0, k-1)#rotat the first k [4,5,6,3,2,1]
        self.reverse(nums, k, n-1)#rotate the r emaining [4,5,6,1,2,3]
    def reverse(self,nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
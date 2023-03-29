#704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lenght = len(nums)
        i = 0
        j = lenght -1
        while i <= j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            i+=1
            j-=1
        return -1
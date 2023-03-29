#189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums
        new_arr = []
        if k ==0:
            x=1
        else:
            for i in range(len(arr)-k,len(arr)):
                new_arr.append(arr[i])
        for j in range(0,len(arr)-k):
            new_arr.append(arr[j])
        nums = new_arr
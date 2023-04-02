class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        for first in len(numbers):
            for second in numbers:
                sum = first + second 
                if sum:
             
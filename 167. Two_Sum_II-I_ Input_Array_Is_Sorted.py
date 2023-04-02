class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for first in range(len(numbers)):
            for second in range(len(numbers) - first):
                sum = numbers[first] + numbers[second] 
                if sum == target:
                    return [first+1,second+1]
        return []    
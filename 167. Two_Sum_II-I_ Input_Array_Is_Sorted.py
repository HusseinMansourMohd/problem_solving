class Solution:
    
    def two_sum(numbers, target):
    # Initialize two pointers: one at the beginning and one at the end of the array
    left = 0
    right = len(numbers) - 1

    # Iterate until the left pointer is less than the right pointer
    while left < right:
        # Calculate the sum of the elements at the pointers
        current_sum = numbers[left] + numbers[right]

        # If the current sum is equal to the target
        if current_sum == target:
            # Return the indices, incremented by one as the array is 1-indexed
            return [left + 1, right + 1]
        # If the current sum is less than the target
        elif current_sum < target:
            # Move the left pointer to the right
            left += 1
        # If the current sum is greater than the target
        else:
            # Move the right pointer to the left
            right -= 1

    # If no solution is found, return an empty array
    return []   
#The time complexity of this algorithm is O(n), 
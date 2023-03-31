class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize a dictionary to count the frequency of each letter in the string
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        # Initialize the length of the longest palindrome
        length = 0
        
        # Iterate through the frequency of each letter and count the number of letters that appear an   even number of times
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
        
        # Add one to the length if there is at least one letter that appears an odd number of times
        if any(count % 2 != 0 for count in freq.values()):
            length += 1
        
        # Return the length of the longest palindrome
        return length
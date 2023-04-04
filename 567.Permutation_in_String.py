#567. Permutation in String  #sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
    
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False

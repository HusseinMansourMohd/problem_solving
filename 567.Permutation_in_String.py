#567. Permutation in String  #sliding window
class Solution:
    ###
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
    
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        s1_counter = Counter(s1)
        window_counter = Counter()

        for i in range(s2_len):
            window_counter[s2[i]] += 1


            if i >= s1_len:
                if window_counter[s2[i - s1_len]] == 1:
                    del  window_counter[s2[i - s1_len]]
                else:
                    window_counter[s2[i - s1_len]] -= 1
                
            if window_counter == s1_counter:
                return True
            
        return False
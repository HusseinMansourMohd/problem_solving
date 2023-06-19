#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        seen = set()
        maxlen = 0
        ####

        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                maxlen = max(maxlen,len(seen))
                right +=1
            else :
                seen.remove(s[left])
                left +=1

        return maxlen
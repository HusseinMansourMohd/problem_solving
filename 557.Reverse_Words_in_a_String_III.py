class Solution:
    def reverseWords(self, s: str) -> str:
        strg = []
        strg = s.split(' ')
        out = ""
        for si in strg:
            out +=  si[::-1] + " "
            
        return out[:-1]
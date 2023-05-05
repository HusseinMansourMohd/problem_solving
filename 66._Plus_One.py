class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #####
        n = len(digits)
        carry = 1
        for i in range(n-1,-1,-1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
            else:
                ###
                digits[i] = 0
                ###
        if carry == 1:
            digits.insert(0,1)#0 index , 1 is what we insert
        return digits
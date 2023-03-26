class Solution:
def plusOne(self, digits: List[int]) -> List[int]:
    digits = [1,2,3]
    new_digits = []
    digits = str(digits)#transform list to string
    digits = int(digits)#transform string to int
    digit = digits + 1 #add ont to the integer
    digits = str(digits)
    for i in list(digits):
        new_digits.appened(int(i))
    return new_digits
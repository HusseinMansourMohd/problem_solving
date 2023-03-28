Class Solution:
    def combine(self , n :int, k: int) -> List[List[int]]:
        def backtrack(start, comb, k): # take start , list and k number 0f premutations
            if k == 0: # if number of premution is now zero append results

                result.append(list(comb))

                return
            
            for i in range(start, n+1):
                comb.append(i) #append the first number 

                backtrack(i+1, comb, k-1)# backtrak 2 and k =1

                comb.pop()
        result = []

        backtrack(1, [], k)

        return result
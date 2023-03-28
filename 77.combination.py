Class Solution:
    def combine(self , n :int, k: int) -> List[List[int]]:
        def backtrack(start, comb, k):
            if k == 0:
                result.append(list(comb))
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb, k-1)
                comb.pop()
        result = []
        backtrack(1, [], k)
        return result
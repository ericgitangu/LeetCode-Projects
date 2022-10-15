class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x = bin(n)[2:][::-1]
        powers = []
        for i, b in enumerate(x):
            val = int(b)
            if val:
                powers.append(val*(2**i))
        ans = []
        for query in queries:
            power = 1
            for i in range(query[0], query[1]+1):
                power *= powers[i]
            ans.append(power%((10**9) +7))   
        return ans
            
            
        
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x = bin(n)[2:][::-1]
        powers = []
        for i, b in enumerate(x):
            val = int(b)
            if val:
                powers.append(val*(2**i))
        ans = [math.prod(powers[l:r+1])%((10**9) +7) for l, r in queries]
        return ans
            
            
        
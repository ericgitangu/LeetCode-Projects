class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [int(b)*2**i for i, b in enumerate(bin(n)[2:][::-1]) if int(b)]
        ans = [math.prod(powers[l:r+1])%((10**9) +7) for l, r in queries]
        return ans
            
            
        
class Solution:
    def climbStairs(self, n: int) -> int:
        
        steps = [1, 2]
        cache = {}
        
        def dp(m, cache):
            
            if m in cache:
                # print('Optimized')
                return cache.get(m)
            
            if m == 0:
                return 1
            
            elif m > n or m < 0:
                return 0
            
            ways = 0
            for step in steps:
                ways += dp(m - step, cache)
            
            cache[m] = ways
            return ways
        return dp(n, cache)
            
class Solution:
    def reverse(self, x: int) -> int:
        # 1 2 3 4 5
        # 45
        rev = 0
        
        neg = False
        
        if x < 0:
            neg = True
            x *= -1
        
        while x != 0:
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop
            
        if(abs(rev) > (2 ** 31 - 1)):
            return 0
        elif neg:
            return -rev
        else:
            return rev
                
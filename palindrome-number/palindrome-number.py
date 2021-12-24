class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp, rev = x, 0
        
        if x < 0:
            return False
        
        pop = 0
        while x != 0:
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop

        if tmp + rev == tmp * 2:
            return True
        else:
             return False
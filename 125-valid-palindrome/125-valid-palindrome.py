class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub('[^0-9a-zA-Z]+','',s.lower())
        return ''.join(reversed(t)) == t
        
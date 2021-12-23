class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            sets = set()
            sets.add(s[i])
            for j in range(i+1, len(s)):
                if s[i] != s[j] and s[j] not in sets:
                    sets.add(s[j])
                else:
                    break
            maximum = len(sets) if len(sets) > maximum else maximum
        return maximum
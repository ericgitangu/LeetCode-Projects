class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for x in zip(*[list(x) for x in strs]):
            if len(set(x)) == 1:
                prefix += x[0]
            else:
                break
        return prefix
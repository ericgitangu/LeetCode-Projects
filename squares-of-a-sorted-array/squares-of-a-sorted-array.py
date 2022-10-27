class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = [n**2 for n in nums if n >= 0]
        neg = [n**2 for n in nums if n < 0][::-1]
        index = 0
        res = []
        while len(pos) and len(neg):
            if pos[index] < neg[index]:
                res.append(pos.pop(index))
            else:
                res.append(neg.pop(index))
        if len(pos):
            res += pos
        if len(neg):
            res += neg
        return res
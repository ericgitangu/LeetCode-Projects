class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, mx = 0, len(height) - 1, -math.inf
        while left < right:
            mx = max(mx, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                if height[right - 1] < height[left - 1]:
                    right -= 1
                else:
                    left += 1
            # print(left, right)
        return mx
            
            
        
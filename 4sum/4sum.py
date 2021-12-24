class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = set()
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                start = j + 1
                stop = len(nums) - 1
                while start < stop:
                    if nums[i] + nums[j] + nums[start] + nums[stop] == target:
                        soln.add(tuple([nums[i], nums[j], nums[start], nums[stop]]))
                        start += 1
                        stop -= 1
                        continue
                    if nums[i] + nums[j] + nums[start] + nums[stop] < target:
                        start += 1
                    else:
                        stop -= 1
        return list(soln)
        
                
        
        
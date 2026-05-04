class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        end = len(nums)       
        for j in range(0, end+1):
            if j not in nums:
                return j

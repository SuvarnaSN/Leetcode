class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # we can calculate the sum of the array from index 0 to the current index
        prefixSum = [0] * len(nums)
        pivotIndex = -1
        left = 0
        right = 0
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        print(prefixSum)
        for i in range(0, len(nums)):
            if i == 0:
                left = 0
                right = prefixSum[-1] - nums[0] 
            else:               
                left = prefixSum[i-1]
                right = prefixSum[-1] - left - nums[i]

            if left == right:
                pivotIndex = i
                break
        return pivotIndex  
            
        

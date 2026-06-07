class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 0
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum < ans:
                ans = running_sum
        
        return (ans*-1) + 1
            
        
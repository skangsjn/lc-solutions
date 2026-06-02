class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = start = end = 0
        
        for i in range(k):
            curr += nums[i]
            end += 1
        ans = curr
        
        while end <= len(nums)-1:
            curr += nums[end] - nums[start]
            ans = max(ans, curr)
            
            start += 1
            end += 1
            
        return ans / k

            
            
            
            
            
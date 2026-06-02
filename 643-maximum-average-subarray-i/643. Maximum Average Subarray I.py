class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summation = start = end = 0
        
        for i in range(k):
            summation += nums[i]
            end += 1
        max_avg = summation / k
        
        while end <= len(nums)-1:
            summation += nums[end] - nums[start]
            max_avg = max(max_avg, summation / k)
            
            start += 1
            end += 1
            
        return max_avg

            
            
            
            
            
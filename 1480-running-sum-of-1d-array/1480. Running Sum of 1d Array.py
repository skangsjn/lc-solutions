class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_sum = [nums[0]]
        
        for i in range(1, len(nums)):
            ans = nums_sum[-1] + nums[i]
            nums_sum.append(ans)
            
        return(nums_sum)
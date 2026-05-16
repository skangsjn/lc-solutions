class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        mpp = {}

        for i in range(n):
            if target - nums[i] in mpp:
                return [mpp[target-nums[i]], i]
            
            mpp[nums[i]] = i
        
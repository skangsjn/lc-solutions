class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = {}
        l = ans = 0

        for r in range(len(nums)):
            counts[nums[r]] = counts.get(nums[r], 0) + 1

            while counts[nums[r]] > k:
                counts[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans
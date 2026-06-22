class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = total_score = l = 0
        elements = set()

        for r in range(len(nums)):
            while nums[r] in elements:
                elements.remove(nums[l])
                total_score -= nums[l]
                l += 1

            elements.add(nums[r])
            total_score += nums[r]
            ans = max(ans, total_score)
        
        return ans
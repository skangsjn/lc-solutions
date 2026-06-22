from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        l = curr = ans = 0

        for r in range(len(nums)):
            curr += nums[r]
            
            if curr - goal in counts:
                ans += counts[curr - goal]
            counts[curr] += 1

            # print(counts, ans)

        return ans
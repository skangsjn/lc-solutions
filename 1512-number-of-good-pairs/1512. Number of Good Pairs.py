from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0

        for v in counts.values():     
            if v > 1:
                ans += (v*(v-1) // 2)
        
        return ans
        
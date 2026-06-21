from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        
        for i in nums:
            counts[i] += 1
        
        print(counts)
            
        if 1 not in set(counts.values()):
            return -1
        
        for key, value in counts.items():
            if value == 1 and key > ans:
                ans = key
            
        return ans            
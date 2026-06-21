class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        ans = -1

        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        for k, v in counts.items():
            if k == v:
                ans = max(ans, k)
        
        return ans
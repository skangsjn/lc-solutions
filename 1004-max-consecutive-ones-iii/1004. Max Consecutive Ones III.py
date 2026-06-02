class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = flips = ans = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                flips += 1
                            
            while flips > k:
                if nums[start] == 0:
                    flips -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
            end += 1 
                            
        return ans
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        total = 0

        for k, v in counts.items():
            if v == 1:
                total += k

        return total
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        max_freq = total_freq = 0

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

            if counts[num] > max_freq:
                 max_freq = counts[num]
                 total_freq = counts[num]
            elif counts[num] == max_freq:
                total_freq += counts[num]
        
        return total_freq
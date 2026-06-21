class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        max_freq = ans = 0

        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
            # print(counts)
            max_freq = max(max_freq, counts[nums[i]])
        print(max_freq)
        
        for k, v in counts.items():
            if v == max_freq:
                ans += v
        
        return ans
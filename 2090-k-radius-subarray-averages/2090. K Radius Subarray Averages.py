class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sum_array = [nums[0]]
        avg_array = [-1] * len(nums)
        start = 0
        
        for i in range(1, len(nums)):
            sum_array.append(sum_array[-1] + nums[i])
        
        for i in range(k, len(sum_array) - k):
            if i == k:
                avg_array[i] = sum_array[i+k] // ((2*k )+ 1)
            else:
                avg_array[i] = (sum_array[i+k] - sum_array[i-k-1]) // ((2*k )+ 1)
        return avg_array          
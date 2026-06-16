class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        arr = []

        for i in range(len(nums)):
            total += nums[i]
            arr.append(total)
        print(arr)

        if arr[-1] - nums[0] == 0:
            return 0
                
        for i in range(1, len(arr)):
            if arr[-1] - arr[i] == arr[i-1]:
                return i
        
        return -1

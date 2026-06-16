class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr +=1

        # zero_idx = 0
        # for i in range(len(nums)):
        #     # print(nums[i])
        #     if nums[i] == 0:
        #         zero_idx = i
        #     if nums[i] != 0 and nums[zero_idx] == 0:
        #         nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
        #         zero_idx = i
        #     print(nums)
        #     print(zero_idx)

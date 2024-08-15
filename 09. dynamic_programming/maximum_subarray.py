'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''


class Solution:
    def maxSubArray(self, nums) -> int:

        if len(nums) == 1:
            return nums[0]

        max_subarray, curr_res = nums[0], nums[0]

        for i in range(1, len(nums)):

            if nums[i] + curr_res > nums[i]:
                curr_res += nums[i]

            else:
                curr_res = nums[i]

            if curr_res > max_subarray:
                max_subarray = curr_res

        return max_subarray

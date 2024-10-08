'''You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.'''


class Solution:
    def rob(self, nums) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        res_arr = [0] * len(nums)
        res_arr[0] = nums[0]
        res_arr[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res_arr[i] = max(nums[i] + res_arr[i-2], res_arr[i-1])

        return res_arr[-1]

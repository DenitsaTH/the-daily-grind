'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


# Version one: use dict to keep track of passed values and their indices

class Solution:
    def twoSum(self, nums, target):
        vals = {}

        for i in range(len(nums)):
            res = target - nums[i]

            if res in vals:
                return [i, vals[res]]
            
            vals[nums[i]] = i

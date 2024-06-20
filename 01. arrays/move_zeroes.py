'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

class Solution:
    def moveZeroes(self, nums):

        curr_zero_seq = 0

        for i in range(len(nums)):
            
            if nums[i] != 0:
                for k in range(curr_zero_seq):
                    nums[i-k], nums[i-1-k] = nums[i-1-k], nums[i-k]
            else:
                curr_zero_seq += 1

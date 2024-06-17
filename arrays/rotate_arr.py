from typing import List


'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k % n  # handles k larger than list length
        
        nums[:] = nums[-k:] + nums[:-k]

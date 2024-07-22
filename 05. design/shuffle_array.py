'''Given an integer array nums, design an algorithm to randomly shuffle the array. 
All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.'''

import random


class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = nums

    def reset(self):
        self.nums = self.original
        return self.nums

    def shuffle(self):
        self.nums = []

        for _ in range(len(self.original)):
            curr = random.choice(self.original)
            while curr in self.nums:
                curr = random.choice(self.original)

            self.nums.append(curr)

        return self.nums


# Test
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_2)
print(param_1)

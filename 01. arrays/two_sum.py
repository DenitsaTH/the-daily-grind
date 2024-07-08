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


# Version two: sort the array and use binary search for O(log n) time complexity
# Downside is that this solution also requires additional memory to keep the original pre-sorting indices

class Solution:
    def twoSum(self, nums, target):

        def binary_search(start, stop, x):

            while start <= stop:

                mid = start + (stop - start) // 2

                if nums_with_indices[mid][0] == x:
                    return nums_with_indices[mid][1]

                elif nums_with_indices[mid][0] < x:
                    start = mid + 1

                else:
                    stop = mid - 1

            return

        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort()

        for i in range(len(nums_with_indices)):
            res = target - nums_with_indices[i][0]

            found = binary_search(i+1, len(nums_with_indices) - 1, res)

            if found is not None:
                return [nums_with_indices[i][1], found]

        return []

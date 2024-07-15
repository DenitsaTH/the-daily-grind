'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.'''


# O(n * (n + m))

def merge(nums1, m: int, nums2, n: int) -> None:
    if m == 0:
        nums1[:n] = nums2[:n]
        return

    nums2_el_counter = 0

    for i in range(m + n):

        if nums2_el_counter < n and (i >= m + nums2_el_counter or nums1[i] > nums2[nums2_el_counter]):
            nums1.insert(i, nums2[nums2_el_counter])
            nums1.pop()
            nums2_el_counter += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums # but it is optional since the modification is done in place I think

"""
# using seeker and placeholder as follows which is form .., which is more efficient

def moveNonZeroes(nums):
    holder = 0
    seeker = 0

    while seeker < len(nums):
        if nums[seeker] != 0:
            nums[holder], nums[seeker] = nums[seeker], nums[holder]
            holder += 1
        seeker += 1
"""

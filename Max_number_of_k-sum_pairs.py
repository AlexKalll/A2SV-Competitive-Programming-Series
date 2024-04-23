class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r, counter = 0, n-1, 0
        nums.sort()

        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum == k:
                counter += 1
                l += 1
                r -= 1
            elif cur_sum < k:
                l +=1
            else:
                r -= 1
        return counter


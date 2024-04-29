class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        total = 0
        for i in range(k):
            total += nums[i]
        max_avg = total / k

        left = 0
        right = k

        while right < len(nums):
            total -= nums[left]
            total += nums[right]
            left += 1
            right += 1
            max_avg = max(max_avg, total/k)
            
        return max_avg

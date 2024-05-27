class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        mp ={0:1}
        ans = 0 
        for num in nums:
            curr_sum += num
            x = curr_sum -k
            if x in mp:
                ans += mp[x]
            mp[curr_sum] = mp.get(curr_sum, 0) + 1
        return ans
        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def check(j):
            if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                return True
            return False
        
        # bubble sort to arrange the numbers
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if check(j):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # Convert the sorted numbers to a string and putting them together which is the largest number
        result = ''.join(map(str, nums))
        # If the result is empty, return '0'
        if int(result) == 0:
            return '0'
        return result
       

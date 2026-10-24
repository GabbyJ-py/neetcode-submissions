class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            prev2, prev = prev, max(prev, nums[i]+prev2)

        return prev
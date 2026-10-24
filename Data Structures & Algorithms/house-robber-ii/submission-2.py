class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        prev2 = nums[1]
        prev = max(nums[1], nums[2])

        for i in range(3,len(nums)):
            prev2, prev = prev, max(prev, nums[i]+prev2)

        sol1 = prev

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2,len(nums)-1):
            prev2, prev = prev, max(prev, nums[i]+prev2)

        sol2 = prev

        return max(sol1, sol2)


        
        
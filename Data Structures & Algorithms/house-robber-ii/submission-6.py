class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def rob(start, end):
            prev2 = 0
            prev = 0

            for i in range(start,end):
                prev2, prev = prev, max(prev, nums[i]+prev2)

            return prev

        sol1 = rob(0, len(nums)-1)
        sol2 = rob(1, len(nums))

        return max(sol1, sol2)



        
        
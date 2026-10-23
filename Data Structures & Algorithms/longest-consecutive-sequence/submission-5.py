class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 0
        maxi = 0
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                res += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                maxi = max(maxi,res+1)
                res = 0
        
        return max(maxi,res+1)

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) 
        suffix = [1] * len(nums) 

        pre = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = pre
            pre *= nums[i]

        suf = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suf
            suf *= nums[i]            

        return [prefix[i]*suffix[i] for i in range(len(nums))]


        
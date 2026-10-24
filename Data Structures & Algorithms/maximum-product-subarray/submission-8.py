class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sofar = float("-inf")
        left_prod = 1
        right_prod = 1
        for i in range(len(nums)):

            left_prod *= nums[i] 
            right_prod *= nums[len(nums)-1-i] 

            max_sofar = max(max_sofar,left_prod,right_prod)

            if nums[i] == 0:
                left_prod = 1
            if nums[len(nums)-i-1] == 0:
                right_prod = 1
            
        return max_sofar

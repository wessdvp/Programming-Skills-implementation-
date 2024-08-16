class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # constraints
        if not 1 <= len(nums)  <= 10**5:
            print("nums length should be between 1 and 10^5")
            return None
        if not all(-10**5 <= i <= 10**5 for i in nums):
            print("each integer in nums should be between -10^5 and 10^5")
            return None
        # logic
        increasing = decreasing = True
        for i in range (len(nums) - 1):
            if nums[i+1] > nums[i]:
                increasing = False
            elif nums[i+1] < nums[i]:
                decreasing = False
        return increasing or decreasing

        

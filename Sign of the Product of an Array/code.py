class Solution:
    def signFunc (self, x: int) -> int:
        if x > 0:
            return 1
        if x < 0:
            return -1
        if x == 0:
            return 0
    def arraySign(self, nums: List[int]) -> int:
        # verify constraints
        if not 1 <= len(nums) <= 1000:
            print("nums should be between 1 and 1000")
            return None
        if not all(-100 <= i <= 100 for i in nums):
            print("each value in nums should be between -100 and 100")
            return None
        # logic
        product = 1
        for i in range (len(nums)):
            product *= nums[i]
        return self.signFunc(product)

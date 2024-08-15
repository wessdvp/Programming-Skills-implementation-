class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # constraints
        if not (1 <= len(nums) <= (10 ** 4)):
            print("nums length should be between 1 and 10^4")
            return None

        # Initialize a pointer for the last non-zero element
        last_non_zero_index = 0

        # First pass: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        # Second pass: Fill the remaining positions with zeros
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # constraints
        if not (1 <= len(digits) <= 100):
            print("digits length should be between 1 and 100")
            return None
        if not (all(0 <= i <= 9 for i in digits)):
            print("digit should be between 0 and 9")
            return None
        if len(digits) > 1 and digits[0] == 0:
            print("digits should not contain any leading 0's")
            return None
        # convert list to int
        num = int("".join(map(str, digits)))
        num += 1
        # convert back
        digits = [int(digit) for digit in str(num)]
        return digits

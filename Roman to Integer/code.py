class Solution:
    def romanToInt(self, s: str) -> int:
        # initialize dictionary
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # constraints
        # check validity
        if not all(char in roman_to_int for char in s):
            return None
        # check length
        if not 1 <= len(s) <= 15:
            print("the length of s should be between 1 and 15")
            return None
        # logic
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_to_int[char]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value

        # Check if the final value is within the valid range [1, 3999]
        if not (1 <= total <= 3999):
            return None

        return total
        

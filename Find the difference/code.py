from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if len(s) == 0:
            if not (len(t) == len(s) + 1):
                print("Warning: 't' should have a length of s plus one character")
                return None
            if not (t.islower() and t.isalpha()):
                print("Warning: Both words must be strictly lowercase English letters.")
                return None

        else:
            # Validate inputs
            if not (0 <= len(s) <= 1000):
                print("Warning: 's' should have a length between 0 and 1000")
                return None
            if not (len(t) == len(s) + 1):
                print("Warning: 't' should have a length of s plus one character")
                return None
            if not (s.islower() and t.islower() and s.isalpha() and t.isalpha()):
                print("Warning: Both words must be strictly lowercase English letters.")
                return None

        # Use Counter to count occurrences of each character
        count_s = Counter(s)
        count_t = Counter(t)

        # Find the character that is in t but not in s or has an extra count in t
        for char in count_t:
            if count_t[char] > count_s.get(char, 0):
                return char

        return None

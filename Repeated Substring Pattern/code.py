class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # constraints
        if not (1 <= len(s) <= 5 * (10 ** 4)):
            print("s length should be between 1 and 5 * 10^4")
            return None
        if not (1 <= len(t) <= 5 * (10 ** 4)):
            print("t length should be between 1 and 5 * 10^4")
            return None

        # Validate that strings consist of only lowercase English characters
        if not s.isalpha() or not t.isalpha():
            print("The words should consist of only English characters")
            return None
        if not s.islower() or not t.islower():
            print("The words should consist of only lowercase English characters")
            return None
        # logic
        from collections import Counter
        return Counter(s) == Counter(t)

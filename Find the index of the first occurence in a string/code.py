class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    # validate
        if not 1 <= len(haystack) <= 10**4:
            print("haystack length should be between 1 and 10^4")
            return None
        if not 1 <= len(needle) <= 10**4:
            print("needle length should be between 1 and 10^4")
            return None
        if not haystack.isalpha() and needle.isalpha():
            print ("the words should consist of only english characters")
            return None
        if not haystack.islower() and needle.islower():
            print ("the words should consist of only english characters")
            return None
        return haystack.find(needle)

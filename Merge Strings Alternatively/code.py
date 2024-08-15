class Solution:
    def __init__(self):
        pass

    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Validate inputs
        if not (1 <= len(word1) <= 100) or not (1 <= len(word2) <= 100):
            raise ValueError("Both words must have a length between 1 and 100.")
        if not (word1.islower() and word2.islower()):
            raise ValueError("Both words must be strictly lowercase English letters.")
        if not (word1.isalpha() and word2.isalpha()):
            raise ValueError("Both words must contain only English letters.")

        # Initialize pointers for both strings
        i, j = 0, 0
        merged = []

        # Interleave characters from both strings
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from the longer string
        while i < len(word1):
            merged.append(word1[i])
            i += 1

        while j < len(word2):
            merged.append(word2[j])
            j += 1

        # Join the list into a string and return
        return ''.join(merged)

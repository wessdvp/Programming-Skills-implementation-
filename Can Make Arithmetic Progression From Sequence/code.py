class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    # constraints
        if not 2 <= len(arr) <= 1000:
            print("arr length should be between 2 and 1000")
            return None
        if not all(-10**6 <= i <= 10**6 for i in arr):
            print("each num in arr should be between -10^6 and 10^6")
            return None
    #logic
        arr.sort()
        index_set = arr[1]-arr[0]
        for i in range (1, len(arr)):
            if arr[i] - arr[i-1] != index_set:
                return False
        return True

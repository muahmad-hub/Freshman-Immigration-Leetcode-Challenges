class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = s.copy()
        for i in range(len(s)):
            s[i] = x[-(i+1)]

    